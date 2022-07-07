from distutils.command.clean import clean
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 9999
client.connect((host,port))
client.sendall(b'Hello World!')
data = client.recv(1024)
client.close()
print('Received',repr(data))