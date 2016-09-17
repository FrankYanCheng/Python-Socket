#coding:utf8
import socket
import time
import threading
import sys
import select
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
	
	def socketSend(self):
		while True:
			send_message=raw_input()
			#send_message=raw_input()
			self.client_socket.sendall(self.nickname+":"+send_message)
			
	def start(self):
		self.socketConnect()
		inputs=[self.client_socket]
		outputs=[sys.stdin]
		while True:
			socket_ready,write_ready,except_change=select.select(inputs,outputs,[])
			for s in socket_ready:
				data=self.client_socket.recv(1024)
				print data
			for message_list in write_ready:
				for send_message in message_list:
					self.client_socket.sendall(self.nickname+":"+send_message)
					
	def closeSocket(self):
		self.client_socket.close()

if __name__=='__main__':
	address='127.0.0.1'
	port=5004
	print 'Please input your nickname.......'
	nickname=raw_input()
	client=Client(address,port,nickname)
	#try:
	client.start()
	#except:
	#client.closeSocket()
	
	
				
		
	
		
		
