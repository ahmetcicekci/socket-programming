from socket import *
import threading


serverPort = 12000
serverName = gethostbyname(gethostname())

clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName,serverPort))


class ThreadedClient():

	isNewConnection = True

	def listenToServer(self):
		while True:
			message = clientSocket.recv(1024).decode("utf-8")
			print ("", message)


	def __init__(self):

		while True:

			if self.isNewConnection:
				username = input("Please enter your username: ")
				self.isNewConnection = False
				clientSocket.send("type_username".encode())
				clientSocket.send(username.encode())
			else:
				message = input("")
				clientSocket.send("type_message".encode())
				clientSocket.send(message.encode())

			threading.Thread(target = self.listenToServer, ).start()



if __name__=="__main__":
    ThreadedClient()




