import requests
import base64
import socket
import os
import sys
from bs4 import BeautifulSoup
import re

def callback(targetfile,msg):
    l=re.split("[ \n]+",msg)
    l1=list(filter(None,l))
    myString = ",".join(l1)
    print(myString)
    f = open(targetfile, 'at')
    f.write(myString+"\n")
    f.close()

def parseResponse(resp,callback,targetfile):
    startIndex=resp.find("#")
    if startIndex==-1:
        return -1
    
    resp = resp[startIndex+1:]
    while True:
        endIndex=resp.find("#")
        if endIndex==-1:
            return 0
        fragment=resp[:endIndex]
        callback(targetfile,fragment)
        resp=resp[endIndex+1:]
        
def processExe(exefile,log):
    base = os.path.splitext(exefile)[0]
    fn=os.path.splitext(exefile)[0]+".csv"
    path, file = os.path.split(fn)
    target = os.path.join("csv",file)
    parseResponse(log,callback,target)

def threadFunc(filename,sock1):
    m = sock1.recv(2048)
    l = m.decode()
    #l=""
    #while True:
        #m=sock1.recv(1024)
        #msg=m.decode()
        #print(msg)
        #if len(msg)<2:
            #break
        #else:
            #l=l+msg
    #l={"process_id": "3332", "data": "3332 malware.exe\n#242560000\nLoadLibrary\nlpFileName=C:\\WINDOWS\\system32\\IMM32.DLL\nReturn=76390000\n#243500000\nLoadLibrary\nlpFileName=gdi32.dll\nReturn=77f10000\n#243100000\nLoadLibrary\nlpFileName=LPK.DLL\nReturn=629c0000\n", "sample_hash": "dbb2b11dea9f4432291e2cbefe14ebe05e021940e983a37e113600eee55daa95"}
    print("Obtained from socket")
    print(l)
    index=l.find("data")+6
    subs1=l[index:]
    index1=subs1.find(",")
    log=subs1[:index1]
    #log=l["data"]
    print(log)
    processExe(filename,log)

def requestServer(token,filename):
    file_to_upload=open(filename, mode='rb')
    encoded_string=base64.b64encode(file_to_upload.read())
    submit_data={"file":encoded_string}
    print("File submitted: " + filename)
    response=requests.post(link_url+"submit_file/",headers={'Authorization': 'Token {}'.format(token)},data=submit_data)
    data=response.json()    
    sha=data['SHA-256']
    sha_token={"SHA256":sha}
    hooklog_response=requests.post(link_url+"get_hooklog/",headers={'Authorization': 'Token {}'.format(token)},data=sha_token)
    hooklog_data=hooklog_response.json()
    
    if 'hooklog' in hooklog_data:
        hooklog=hooklog_data['hooklog']
        b64=hooklog[0]['hooklog']
        htm=base64.b64decode(b64)
        soup = BeautifulSoup(htm)
        log=soup.get_text()
        processExe(filename,log)
    else:
        print(hooklog_data)
#def requestServer(token,filename):
    #file_to_upload=open(filename, mode='rb')
    #encoded_string=base64.b64encode(file_to_upload.read())
    #submit_data={"file":encoded_string,"streaming":True}
    #print("File submitted: " + filename)
    #streaming_response=requests.post(link_url+"submit_file/",headers={'Authorization': 'Token {}'.format(token)},data=submit_data)
    #streaming_data=streaming_response.json()    
    #host=streaming_data['server_ip']
    #port=int(streaming_data['server_port'])
    #sha=streaming_data['SHA-256']
    #print("Connecting to socket")
    #try:
        #sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        #sock.connect((host,port))
        #sock.send(sha.encode())
        #threadFunc(filename,sock)
    #except socket.error:
        #print ("Socket error")
    #finally:
        #sock.close()
    # thread = threading.Thread(target=threadFunc,kwargs=dict(sock1=sock))
    # thread.start()

dirr=sys.argv[1]
#username=sys.argv[1]
#password=sys.argv[2]
username="binun"
password="BW~35wc&"

link_url="http://140.112.107.39:80/"
csvdir="csv"   

if not os.path.exists(csvdir):
    os.makedirs(csvdir)

auth_data={'username':username,'password':password}
auth_response=requests.post(link_url+"request_token/",auth_data)
auth_data = auth_response.json()
print(auth_data)
token=auth_data['token']
print("Authenticated")

for filename in os.listdir(dirr):
    requestServer(token,dirr+"/"+filename)
