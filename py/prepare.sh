apt-get -y update
apt-get -y install build-essential checkinstall
apt-get -y install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev
cd /usr/src && wget https://www.python.org/ftp/python/3.6.0/Python-3.6.0.tgz && tar xzf Python-3.6.0.tgz
cd Python-3.6.0
./configure
make install

pip3.6 install requests
python3.6 -m pip install beautifulsoup4
# unrar x -r
#https://forum.tuts4you.com/topic/28114-live-malware-samples/
# trojan win32 malware download
# http://malwaredb.malekal.com/
