# importacao das bibliotecas
import socket
import os.path

# definicao do host e da porta do servidor
HOST = ''  # ip do servidor (em branco)
PORT = 8080  # porta do servidor

# cria o socket com IPv4 (AF_INET) usando TCP (SOCK_STREAM)
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# permite que seja possivel reusar o endereco e porta do servidor caso seja encerrado incorretamente
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# vincula o socket com a porta (faz o "bind" do IP do servidor com a porta)
listen_socket.bind((HOST, PORT))

# "escuta" pedidos na porta do socket do servidor
listen_socket.listen(1)

# imprime que o servidor esta pronto para receber conexoes
print('Serving HTTP on port %s ...' % PORT)

# declaracao das respostas do servidor

# Bad Request
data400 = open("400error.html")
b_r_html = data400.read()
bad_request = "HTTP/1.1 400 Bad Request\r\n\r\n" + b_r_html

# GET
indexdata = open("index.html")
get_html = indexdata.read()
get = "HTTP/1.1 200 OK\r\n\r\n" + get_html

# Not found
data404 = open("404error.html")
n_f_html = data404.read()
not_found = "HTTP/1.1 404 Not Found\r\n\r\n" + n_f_html


while True:
    # aguarda por novas conexoes
    client_connection, client_address = listen_socket.accept()
    # o metodo .recv recebe os dados enviados por um cliente atraves do socket
    request = client_connection.recv(1024)
    # imprime na tela o que o cliente enviou ao servidor
    print(request.decode('utf-8'))
    req = request.decode('utf-8')
    x = req.split(" ")

    # Observação: usando o telnet, no caso 1 se não houver o HTTP/1.1 vai dar not found ao invés do status ok + index.htmtl
    if (x[0] == 'GET'):
        # caso 1: GET /
        if (x[1] == '/'):
                print("Status 200 OK\n")
                client_connection.send(get.encode('utf-8'))
                client_connection.close()
        else:
            # Verificando se arquivo existe
                path = '.'+x[1]
                checkfile = os.path.isfile(path)
                # caso 2: GET arquivo.html
                if (checkfile):
                    # Declaração da resposta para a resposta do servidor no caso 2
                    data = open("."+x[1])
                    caso2_html = data.read()
                    caso2 = "HTTP/1.1 200 OK\r\n\r\n" + caso2_html
                    
                    print("Status 200 OK\n")
                    client_connection.send(caso2.encode('utf-8'))
                    client_connection.close()
                # caso 3: Not found
                else:
                    print("Não encontrado\n")
                    client_connection.send(not_found.encode('utf-8'))
                    client_connection.close()
    # caso 4: Bad request
    else:
        print("Comando não reconhecido\n")
        client_connection.send(bad_request.encode('utf-8'))
        client_connection.close()

    client_connection.close()

# encerra o socket do servidor
listen_socket.close()
