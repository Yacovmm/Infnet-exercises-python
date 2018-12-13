import socket
import pickle
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host, port = socket.gethostname(), 8881


def main():
    s.connect((host, port))


    opcoes = s.recv(4096)
    print(opcoes.decode())
    option = input("Entre a opção desejada: ")

    if option.lower() == 'q':
        print("Saindo")
        s.close()

    s.send(option.encode())

    msg = s.recv(10000)
    print(msg.decode())

    s.close()



if __name__ == '__main__':
    main()
