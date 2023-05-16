# importacao das bibliotecas
from socket import * # sockets
import time 

# definicao das variaveis

systemData = str(time.ctime())
errorMessage = 'Comando nao aceito'

serverName = '' # ip do servidor (em branco)
serverPort = 61000 # porta a se conectar
serverSocket = socket(AF_INET, SOCK_DGRAM) # criacao do socket UDP
serverSocket.bind((serverName, serverPort)) # bind do ip do servidor com a porta
print ('Servidor UDP esperando conexoes na porta %d ...' % (serverPort))
while 1:
    message, clientAddress = serverSocket.recvfrom(2048) # recebe do cliente
    message = message.decode('utf-8')
	
    if message == 'data' :
        print('Cliente solicitou a informacao da data')
        serverSocket.sendto(systemData.encode('utf-8'), clientAddress) # envia a resposta para o cliente
    
    else :
        print('Comando nao aceito')
        serverSocket.sendto(errorMessage.encode('utf-8'), clientAddress) # envia a resposta de erro para o cliente


serverSocket.close() # encerra o socket do servidor