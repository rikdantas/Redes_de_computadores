# importacao das bibliotecas
from socket import *  # sockets

# definicao das variaveis
serverName = ''  # ip do servidor (em branco)
serverPort = 61000  # porta a se conectar
serverSocket = socket(AF_INET, SOCK_STREAM)  # criacao do socket TCP
# bind do ip do servidor com a porta
serverSocket.bind((serverName, serverPort))
serverSocket.listen(1)  # socket pronto para 'ouvir' conexoes

data = open('arquivo.txt')
errorMessage = 'Comando nao aceito'

print('Servidor TCP esperando conexoes na porta %d ...' % (serverPort))
while 1:
    connectionSocket, addr = serverSocket.accept()  # aceita as conexoes dos clientes
    sentence = connectionSocket.recv(1024)  # recebe dados do cliente
    sentence = sentence.decode('utf-8')

    if (sentence == 'obter arquivo.txt'):
        print('Cliente solicitou o conteúdo de arquivo.txt') # envia para o cliente o conteudo de arquivo.txt
        connectionSocket.send(data.read().encode('utf-8'))
        connectionSocket.close()  # encerra o socket com o cliente
    else:
        print(errorMessage)
        connectionSocket.send(errorMessage.encode('utf-8'))
        connectionSocket.close()  # encerra o socket com o cliente

serverSocket.close()  # encerra o socket do servidor
