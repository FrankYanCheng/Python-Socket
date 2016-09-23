'''
Python 2.7 FTP upload and download
'''
from ftplib import FTP
import os
import os.path
import datetime
import getpass

class FTPer:
	def __init__(self,host,user,pwd,direct_name,bufsize):
		self.host=host
		self.user=user
		self.pwd=pwd
		self.direct_name=direct_name
		self.bufsize=bufsize
		self.ftp=self.bind()

	def bind(self):
		ftp=FTP()
		ftp.connect(self.host)
		ftp.login(self.user,self.pwd)
		try:
			self.ftp.mkd(self.direct_name)
		except:
			print 'dir has existed %s' % self.direct_name
		ftp.cwd(self.direct_name)
		return ftp
                
	def _searchFile(self):
		files=set()
		for f in os.listdir(os.getcwd()):
			if os.path.isfile(f):
				files.add(f)
		return files
				
	def ftpUp(self):
		files=self._searchFile()
		for file in files:
			print file
			file_handler=open(file,'rb')
			self.ftp.storbinary('STOR %s' % os.path.basename(file),file_handler,self.bufsize)
		print 'ftp upload has been down'
	
	def ftpDown(self):
		files=self.ftp.nlst()
		for file in files:
			print file
		print 'Please input the file you want to download'
		select_file=raw_input()
		if select_file in files:
			file_handler=open(select_file,'wb').write
			self.ftp.retrbinary('RETR %s' % os.path.basename(select_file),file_handler,self.bufsize)
			print 'ftp file download success'
		else:
			print 'Please input the file that exist in the ftp server'
	
	def close(self):
		self.ftp.quit()

print 'Please input host:'
host=raw_input()
print 'Please print user:'
user=raw_input()
print 'Please input password'
pwd=raw_input()
bufsize=1024
direct_name='ftp_auto'
ftp=FTPer(host,user,pwd,direct_name,bufsize)
print 'upload or download?'
switch_judge=raw_input()
if switch_judge=='upload':
        ftp.ftpUp()
elif switch_judge=='download':
        ftp.ftpDown()
ftp.close()		
		
