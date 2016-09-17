#coding:utf8
import socket
import threading
import Queue
import time
class Server:

	def __init__(self,address,port,listen_counts):
		self.address=address
		self.port=port
		self.listen_counts=listen_counts
		self.list_comm=[]
		self.list_message=Queue.Queue()
		self.sendComm=None
		self.sock=None
		#self.engine=Engine()
	'''
	return service socket,with bind information
	'''
	def binding(self):
		sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		sock_addr=(self.address,self.port)
		sock.bind(sock_addr)
		sock.listen(self.listen_counts)
		self.sock=sock
	
	'''
	send message to all client
	'''
	def socketSend(self):
		while True:
			if self.list_message is not None:
				data=self.list_message.get()
				#send message to all client
				for comm in self.list_comm:
					if comm!=self.sendComm:
							comm.sendall(data)
			time.sleep(1)
	
	'''
	client socket listening
	'''
	def socketListen(self,comm,addrs):
		try:
			while True:
				data=comm.recv(1024)
				self.list_message.put(data)
				print data
				self.sendComm=comm
		except:
			self.list_comm.remove(comm)
			message='{} leave the room'.format(addrs)
			print message
			self.list_message.put(message)
	
	'''
	Start Service
	'''
	def start(self):
		print 'Server open address:{},port:{}'.format(self.address,self.port)
		self.binding()
		thread_send=threading.Thread(target=self.socketSend)
		thread_send.start()
		while True:
			comm,addrs=self.sock.accept()
			self.list_comm.append(comm)
			message="{} has join the room,there have {} people on line".format(addrs,len(self.list_comm))
			self.list_message.put(message)
			print('Connection from ',addrs,'accepted')
			thread_listen=threading.Thread(target=self.socketListen,args=(comm,addrs))
			thread_listen.start()
'''
The core of server
'''
'''
class Engine:
	
	def __init__(self):
		self.di_address_name={}
	
	def addDictionary(self,addrs,nickname)：
		if addrs not in self.di_address_name.keys and nickname!='':
			self.di_address_name[addrs]=nickname
			return True
		else:
			return False
	
	def chatRoomMessage(self,message,addrs,nickname):
		addDictionary(self,addrs,nickname)
		if addrs  in self.di_address_name
			replay_message='{}:{}'.format(self.di_address_name[addrs],message)
		else
			replay_message='{}:{}'.format('anonymous',message)
		return replay_message
		
	def transferMessage(self,stauts_message,addrs,nickname='):
		#status '01' add name 
		status=message[0:2]
		message=status_message[2:len(status_message)-2]
		swithcer={
			'01':chatRoomMessage(self,message,addrs,nickname)
		}
		func=swithcer.get(status)
		return func
'''
if __name__=='__main__':
	address='127.0.0.1'
	port=5003
	listen_counts=10
	server=Server(address,port,listen_counts)
	server.start()