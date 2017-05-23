import requests
import base64
import socket
import os
import sys
from bs4 import BeautifulSoup
import re

def callback(targetfile,msg):
	msg=msg.replace(",", "")
	l=re.split("[ \n]+",msg)
	l1=list(filter(None,l))
	myString = ",".join(l1)
	f = open(targetfile, 'at')
	f.write(msg+"\n")
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

def processExe(exefile,soup):
    base = os.path.splitext(exefile)[0]
    fn=os.path.splitext(exefile)[0]+".hooklog"
    path, file = os.path.split(fn)
    target = os.path.join("csv",file)
    f = open(target, 'wt')
    f.write(soup.get_text())
    f.close()
	
    #parseResponse(soup.get_text(),callback,target)
    #hfn=os.path.splitext(exefile)[0]+".hooklog"
    #pathr, filer = os.path.split(hfn)
    #targetr = os.path.join("csv",filer)
    #f = open(targetr, 'wt')
    #f.write(str(soup))
    #f.close()

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
    #print(hooklog_data)
    if 'hooklog' in hooklog_data:
        hooklog=hooklog_data['hooklog']
        b64=hooklog[0]['hooklog']
        htm=base64.b64decode(b64)
        soup = BeautifulSoup(htm)
        processExe(filename,soup)

dirr=sys.argv[1]
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
