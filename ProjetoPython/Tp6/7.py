
import psutil

import socket


def Main():
    show_redes_info()


def show_redes_info():
    txt = '{:>4}'.format("End.")
    txt += '{:>6}'.format("Tipo")
    txt += '{:>20}'.format("Status")
    txt += '{:>30}'.format("Endereço")
    # txt += '{:>40}'.format("Local")
    # txt += '{:<10}'.format("Porta l.")
    txt += '{:>40}'.format("PID")
    print(txt)
    for i in psutil.net_connections()[0:10]:
        # info = '{:>5} {:>4} {:>19} {:>30} {:>40} \n'.format(obtem_nome_familia(i.family), obtem_tipo_socket(i.type), i.status, i.laddr.ip, i.pid)
        print('{:>5} {:>4} {:>19} {:>30} {:>40}'.format(obtem_nome_familia(i.family), obtem_tipo_socket(i.type), i.status, i.laddr.ip, i.pid))


def obtem_nome_familia(familia):
    if familia == socket.AF_INET:
        return ("IPv4")
    elif familia == socket.AF_INET6:
        return ("IPv6")
    elif familia == socket.AF_UNIX:
        return ("Unix")
    else:
        return ("-")


def obtem_tipo_socket(tipo):
    if tipo == socket.SOCK_STREAM:
        return ("TCP")
    elif tipo == socket.SOCK_DGRAM:
        return ("UDP")
    elif tipo == socket.SOCK_RAW:
        return ("IP")
    else:
        return ("-")

if __name__ == '__main__':
    Main()