#coding:utf8
import socket
import time
import threading
class Client:
		
	def __init__(self,address,port,nickname):
		self.address=address
		self.port=port
		self.client_socket=None
		self.nickname=nickname
	
	def socketConnect(self):
		self.client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		server_addr=(self.address,self.port)
		print 'service address{},port{}'.format(self.address,self.port)
		self.client_socket.connect(server_addr)
		
	def socketReceive(self):
		while True:
			data=self.client_socket.recv(512)
			print data
	
	def socketSend(self):
		while True:
			send_message=raw_input()
			#send_message=raw_input()
			self.client_socket.sendall(nickname+":"+send_message)
	
	def start(self):
		self.socketConnect()
		thread_receive=threading.Thread(target=self.socketReceive)
		thread_receive.start()
		self.socketSend()
	
	def closeSocket(self):
		self.client_socket.close()

if __name__=='__main__':
	address='www.fyc.pub'
	port=5004
	print 'Please input your nickname.......'
	nickname=raw_input()
	client=Client(address,port,nickname)
	try:
		client.start()
	except:
		client.closeSocket()
	
	
				
		
	
		
		
