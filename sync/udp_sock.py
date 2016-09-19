import Queue
import socket
import sys
import threading
class UDP(object):

	def __init__(self):
		print 'Please input the Recive port'
		self.recv_port=input()
		print 'Please input the Send port'
		self.send_port=input()
		print 'Please input the nickname'
		self.nickname=raw_input()
		self.sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
		self.sock.bind((('',self.recv_port)))
		
	
	def Recive(self):
		#sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
		#sock.bind(('',self.recv_port))
		while True:
			recvData,remote_address=self.sock.recvfrom(1024)
			print "{}connect ".format(remote_address)
			print recvData

	def Send(self):
		#sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
		while True:
			data=raw_input()
			self.sock.sendto(self.nickname+":"+data,('127.0.0.1',self.send_port))
		
	def Start(self):
		recv_thread=threading.Thread(target=self.Recive)
		recv_thread.start()
		self.Send()

if __name__=="__main__":
	udp=UDP()
	udp.Start()
