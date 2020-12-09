"""
Description:
Language:Python 2.7
Author:Matthew Stoffolano
"""
import socket
import sys

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

def user_interface():
	"""
	Description: This is what the user can use to decide on a function to be made.
	"""
	command = raw_input("> ")
	if command == "tcp":
		tcp_client()
	elif command == "exit":
		sys.exit()
	else:
		print "You entered " + str(command) + " ,which is a unknwon command."

def main():
	print "Welcome to Client"
	user_interface()

main()
