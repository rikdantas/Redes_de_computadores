# importacao das bibliotecas
from socket import *

# definicao das variaveis
serverName = 'localhost' # ip do servidor
serverPort = 61000 # porta a se conectar
clientSocket = socket(AF_INET,SOCK_STREAM) # criacao do socket TCP
clientSocket.connect((serverName, serverPort)) # conecta o socket ao servidor

command = input('Digite o comando interagir com o servidor remotamente: ')
clientSocket.send(command.encode('utf-8')) # envia o texto para o servidor
receivedData = clientSocket.recv(1024) # recebe do servidor a resposta
print ('O servidor (\'%s\', %d) respondeu com: \n %s' % (serverName, serverPort, receivedData.decode('utf-8')))
clientSocket.close() # encerramento o socket do cliente
