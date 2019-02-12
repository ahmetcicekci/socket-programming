from socket import *
import threading
import datetime

class ThreadedServer():

    connectionSockets = []

    address_username = {}

    def listenToClient(self, connectionSocket, addr):

    	while True: 
    		if connectionSocket not in self.connectionSockets: 
    			self.connectionSockets.append(connectionSocket)

    		type_ = connectionSocket.recv(1024).decode("utf-8")

    		if type_ == "type_username":
    			username = connectionSocket.recv(1024).decode("utf-8")
    			self.address_username[addr[1]] = username
    		else: 
    			message = connectionSocket.recv(1024).decode("utf-8")
    			message = "[" + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "]" + " " + self.address_username[addr[1]] + ": " + message
    			print (message)

    			for c in self.connectionSockets:
    				if c != connectionSocket:
    					c.send(message.encode())
                      


    def __init__(self,serverPort):
        try:
            serverSocket=socket(AF_INET,SOCK_STREAM)
        except:
            print ("Socket cannot be created!!!")
            exit(1)
        print ("Socket is created...")
        try:
            serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        except:
            print ("Socket cannot be used!!!")
            exit(1)
        print ("Socket is being used...")
        try:
            serverSocket.bind(('',serverPort))
        except:
            print ("Binding cannot de done!!!")
            exit(1)
        print ("Binding is done...")
        try:
            serverSocket.listen(45)
        except:
            print ("Server cannot listen!!!")
            exit(1)
        print ("The server is ready to receive")



        while True:

            connectionSocket, addr = serverSocket.accept()
            
            threading.Thread(target = self.listenToClient,args = (connectionSocket, addr)).start()
            

if __name__=="__main__":
    serverPort=12000
    ThreadedServer(serverPort)
	

