import socket
import threading
import sys

PORT = 7500
BUFSIZE = 4096
SERVERIP = '159.65.135.242' # SERVER IP

def server_handler(client):
	global alltext
	while True:
		try:
			data = client.recv(BUFSIZE) # Data from server
		except:
			print('ERROR')
			break
		if (not data) or (data.decode('utf-8') == 'q'):
			print('OUT!')
			break

		alltext = alltext + data.decode('utf-8') + '\n'
		tf.text = ''
		
		history.text = alltext
		history.content_offset = (0,history.content_size[1] - history.height)
			
	client.close()

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

try:
	client.connect((SERVERIP,PORT))
except:
	print('ERROR!')
	sys.exit()

task = threading.Thread(target=server_handler, args=(client,))
task.start()

import ui
import console


global alltext

alltext = ''

def SendButton(sender):
	global alltext
	
	try:
		txt = sender.text
		client.sendall(txt.encode('utf-8'))
		
	except:
		txt = tf.text
		client.sendall(txt.encode('utf-8'))
		

v = ui.load_view()

history = v['history']
tf = v['message']
tf.action = SendButton
tf.begin_editing()

v.present('sheet')
