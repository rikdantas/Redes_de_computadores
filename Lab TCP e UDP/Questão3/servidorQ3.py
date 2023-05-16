# importacao das bibliotecas
from socket import *  # sockets
import subprocess 

# definicao das variaveis
serverName = ''  # ip do servidor (em branco)
serverPort = 61000  # porta a se conectar
serverSocket = socket(AF_INET, SOCK_STREAM)  # criacao do socket TCP
# bind do ip do servidor com a porta
serverSocket.bind((serverName, serverPort))
serverSocket.listen(1)  # socket pronto para 'ouvir' conexoes

print('Servidor TCP esperando conexoes na porta %d ...' % (serverPort))
while 1:
    connectionSocket, addr = serverSocket.accept()  # aceita as conexoes dos clientes
    command = connectionSocket.recv(1024)  # recebe dados do cliente
    command = command.decode('utf-8')
    print('Cliente usou o comando %s ' % (command)) # envia para o cliente o conteudo de arquivo.txt

    command = subprocess.check_output(str(command), shell=True, universal_newlines=True, stderr=subprocess.STDOUT)
    
    connectionSocket.send(command.encode('utf-8'))
    connectionSocket.close()  # encerra o socket com o cliente

serverSocket.close()  # encerra o socket do servidor
