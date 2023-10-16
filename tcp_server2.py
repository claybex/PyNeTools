import socket

IP, PORT = '127.0.0.1', 8080

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP,PORT))
    server.listen(5)
    print(f'[*] Listening on {IP}:{PORT}')

    while True:
        client, cl_addr = server.accept()
        print(f'[*] Accepted connection from {cl_addr[0]}:{cl_addr[1]}')
        with client as sock:
            request = sock.recv(1024)
            print('Recieved request form client:\n{}'.format(request.decode()))
            sock.send(b'ACK')

if __name__ == '__main__':
    main()

