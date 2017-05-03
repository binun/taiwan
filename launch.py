import requests
import base64
import socket
import os
import sys

def callback(f,msg):
    myList=msg.split()
    myString = ",".join(myList)
    print(myString)
    f.write(myString+"\n")

def parseResponse(resp,callback,f):
    startIndex=resp.find("#")
    if startIndex==-1:
        return -1
    
    resp = resp[startIndex+1:]
    while True:
        endIndex=resp.find("#")
        if endIndex==-1:
            return 0
        fragment=resp[:endIndex]
        callback(f,fragment)
        resp=resp[endIndex+1:]
        
def processExe(exefile,resp):
    base = os.path.splitext(exefile)[0]
    fn=os.path.splitext(exefile)[0]+".csv"
    path, file = os.path.split(fn)
    target = os.path.join("csv",file)
    log=resp['data']
    f = open(target, 'at')
    parseResponse(log,callback,f)

def threadFunc(filename,sock1):
    m = sock1.recv(1024)
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
    
    processExe(filename,l)
    
    
def requestServer(token,filename):
    file_to_upload=open(filename, mode='rb')
    encoded_string=base64.b64encode(file_to_upload.read())
    submit_data={"file":encoded_string,"streaming":True}
    
    streaming_response=requests.post(link_url+"submit_file/",headers={'Authorization': 'Token {}'.format(token)},data=submit_data)
    streaming_data=streaming_response.json()
    host=streaming_data['server_ip']
    port=int(streaming_data['server_port'])
    sha=streaming_data['SHA-256']
    try:
        sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.connect((host,port))
        sock.send(sha.encode())
        threadFunc(filename,sock)
    except socket.error:
        print ("Socket error")
    finally:
        sock.close()
    # thread = threading.Thread(target=threadFunc,kwargs=dict(sock1=sock))
    # thread.start()

username=sys.argv[1]
password=sys.argv[2]
link_url="http://140.112.107.39:80/"
maldir="malware"
bendir="benign"    
csvdir="csv"

auth_data={'username':username,'password':password}
auth_response=requests.post(link_url+"request_token/",auth_data)
auth_data = auth_response.json()
token=auth_data['token']

if not os.path.exists(csvdir):
    os.makedirs(csvdir)
else:
    filelist = [ f for f in os.listdir(csvdir) ]
    for f in filelist:
        os.remove(f)

dirr=bendir
for filename in os.listdir(dirr):
    requestServer(token,dirr+"/"+filename)