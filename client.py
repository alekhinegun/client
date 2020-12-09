"""
Description:
Language:Python 2.7
Author:Matthew Stoffolano
"""
import socket
import sys
import threading

command_list = ["client_tcp", "client_udp", "server_tcp", "server_udp", "exit"]

def get_target_info():
	"""
	Description: This is used to retrieve the infomration from the user such as the host and port. 
	return(string:host, int:port)
	"""
	host = raw_input("Enter Host:")
	port = raw_input("Enter Port:")
	return host, int(port)

def udp_client():
	"""
	Description: The function creates a basic udp connection and allows for the continues messages to be sent if you want to send to a new connection then the client must be restarted
	"""
	host = ""
	port = 0
	host, port = get_target_info()
	client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	request = ""
	try:
		host, port = get_target_info()
		while request != "exit":
			request = raw_input(">") 
                        if request == "exit":
                                break
			client.sendto(request, (host, port))
			data, addr = client.recvfrom(4096)
			print "Sent from: " + addr + "\nInformation: " + data
	except:
		print "The connection did not work"

def tcp_client():
	"""
	Description;This creates a TCP connection and will continue to send a recive data.
	"""
	host = ""
	port = 0
	host, port = get_target_info()
	client = socket.socket()
	try:
		client.connect((host, port))
		request = ""
		while request != "exit":
			request = raw_input(">")  
                        if request == "exit":
                                break
			client.send(request)
			print client.recv(4096)
		client.close()
	except:
		print "The connection was not able to be created."
def server_threading(connection):
        print connection.recv(4096)
	connection.socket()
	connection.send("ACK")
	connection.close()

def server_threading_udp(connection):
	print conenction.recvfrom(4096)
	connection.sendto(bytesToSend, address)

def tcp_server():
	host, port = get_target_info()
	server = socket.socket()
	server.bind((host, port))
	server.listen(5)
	while True:
		client, addr = server.accept()
		connection_thread = threading.Thread(target = server_threading, args=(client,))
		connection_thread.start()

def udp_server():
	host, port = get_target_info()
	server =socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	server.bind((host, port))
	while True:
		connection_thread = threading.Thread(target = server_threading_udp, args=(server,))

def help():
	print "Commands:"
	for i in range(0, len(command_list)):
		print command_list[i]

def user_interface():
	"""
	Description: This is what the user can use to decide on a function to be made.
	host, port = get_target_info()
        server = socket.socket()
        server.bind((host, port))
        server.listen()
        print server.client_socket.recv(4096)
"""
	command = ""
	while command != "exit":
		command = raw_input("> ")
		if command == "client_tcp":
			tcp_client()
		elif command == "client_udp":
			udp_client()
		elif command == "server_tcp":
			tcp_server()
		elif command == "server_udp":
			udp_server()
		elif command == "help":
			help()
		elif command == "exit":
			sys.exit()
		else:
			print "You entered " + str(command) + " ,which is a unknwon command."

def main():
	print "Welcome to Client"
	user_interface()

main()
