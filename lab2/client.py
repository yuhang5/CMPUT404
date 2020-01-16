import socket, sys
def create_tcp_socket():
	print("creating socket")
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	except (socket.error, msg):
		print('Failed. Error code:,' + str(msg[0]) + ', Error message : ' + msg[1])
		sys.exit()
	print('socket created successfully')
	return s

def get_remote_ip(host):
	print('Getting IP for ' + host)
	try:
		remote_ip = socket.gethostbyname( host )
	except socket.gaierror:
		print('Hostname could not be resolved. Exiting')
		sys.exit()

	print('IP address of ' + host + ' is ' + remote_ip)
	return remote_ip

def send_data(serversocket, payload):
	print('Sending payload')
	try: 
		serversocket.sendall(payload.encode())
	except socket.error:
		print('Send failed')
		sys.exit()
	print('Payload sent successfully')

def main():
	try:
		host = 'www.google.com'
		port = 80
		payload = 'GET / HTTP/1.0\r\nHost: ' + host + '\r\n\r\n'
		buffer_size = 4096
		s = create_tcp_socket()
		remote_ip = get_remote_ip(host)
		s.connect((remote_ip, port))
		print('Socket connected to ' + host + ' on ip ' + remote_ip)
		send_data(s, payload)
		s.shutdown(socket.SHUT_WR)
		full_data = b""
		while True:
			data = s.recv(buffer_size)
			if not data:
				break
			full_data += data
		print(full_data)
	except Exception as e:
		print(e)
	finally:
		s.close()


if __name__ == "__main__":
	main()