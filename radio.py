import 


def netsend(msg):
	IP="127.0.0.1"
	PORT=3000
	addr=(IP, PORT)
	EOL=';\n'
	sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect((IP,PORT))
	sock.sendto(msg+EOL, addr)
	sock.close()