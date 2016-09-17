#coding:utf8
import socket
import threading
import Queue
import time
import select
class Server:

	def __init__(self,address,port,listen_counts):
		self.address=address
		self.port=port
		self.listen_counts=listen_counts
		self.list_comm=[]
		self.list_message=Queue.Queue()
		self.sendComm=None
		self.sock=None
		
	'''
	return service socket,with bind information
	'''
	def binding(self):
		sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		sock.setblocking(False)
		sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
		sock_addr=(self.address,self.port)
		sock.bind(sock_addr)
		sock.listen(self.listen_counts)
		self.sock=sock
	
	'''
	Start Service
	'''
	def start(self):
		print 'Server open address:{},port:{}'.format(self.address,self.port)
		self.binding()
		send_message=None
		inputs=[self.sock]
		output=[]
		while True:
			#--------------------------------socket listen-------------------------------------#
			sock_ready, out_ready, except_ready = select.select(inputs,[],[])
			for s in sock_ready:
				if s is self.sock:
					per_comm,addrs=s.accept()
					self.list_comm.append(per_comm)
					print('Connection from ',addrs,'accepted')
					message="{} has join the room,there have {} people on line".format(addrs,len(self.list_comm))
					self.list_message.put(message)
					per_comm.setblocking(0)
					inputs.append(per_comm)
					
				else:
					try:
						data=s.recv(1024)
						print data
						self.list_message.put(data)
						self.sendComm=s
					except:
						self.list_comm.remove(s)
						except_data='{} has leave the room'.format(s.getpeername())
						print except_data
						self.list_message.put(except_data)
						inputs.remove(s)
						s.close()
			#--------------------------------message send----------------------------------------#
			if self.list_message is not None:
				data=self.list_message.get()
				#send message to all client
				for comm in self.list_comm:
					if comm!=self.sendComm:
							comm.sendall(data)
				
if __name__=='__main__':
	address='127.0.0.1'
	port=5004
	listen_counts=10
	server=Server(address,port,listen_counts)
	server.start()
