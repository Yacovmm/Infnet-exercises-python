import socket
import os
import psutil
import cpuinfo
import time


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host, port = ('0.0.0.0'), 8881



    opcoes = '''
    ------** Tp 4 / 5 **------
    (a) - Info sobre disco
    (b) - Info sobre cpu / memoria
    (c) - Ip da maquina    
    ------** Tp 6 / 7 **------
    (d) - Info de arquivos/diretorios
    (e) - Info de processos
    (f) - Info de interfaces de rede
    
    (q) Quit
    '''

    try:
        s.bind((host, port))
        s.listen(5)
        print("Servidor de nome %s esperando conexão na gate %s" % (host, port))

        while True:
            (client, addr) = s.accept()

            # Todo: Enviando opçoes ao cliente
            client.send(opcoes.encode())

            opcaoReceived = client.recv(1024)
            recebido = opcaoReceived.decode('utf-8')

            if recebido.lower() == 'a':
                client.send(show_disco_info().encode())
            elif recebido.lower() == 'b':
                client.send(show_memory_use().encode() + mostra_info_cpu().encode())
            elif recebido.lower() == 'c':
                client.send(str(psutil.net_if_addrs()).encode())
            elif recebido.lower() == 'd':
                client.send(str(get_files_info()).encode())
            elif recebido.lower() == 'e':
                client.send(str(get_pids()).encode())
            elif recebido.lower() == 'f':
                client.send(show_redes_info().encode())
            else:
                client.send("Opção errada, servidor sendo fechado!".encode())
                s.close()



    except Exception:
        print("ERRO")
    s.close()


# def mostra_uso_cpu(l_cpu_percent):
#     num_cpu = len(l_cpu_percent)


# todo : Mostrar uso de memória
def show_memory_use():
    mem = psutil.virtual_memory()
    mem_text = "\nPorcentagem: " + str(mem.percent) + '%'
    total = round(mem.total / (1024 * 1024 * 1024), 2)
    usado = round(mem.used / (1024 * 1024 * 1024), 2)
    texto_barra = "Uso de Memória (Total: " + str(total) + "GB): "
    txt = texto_barra + str(usado) + " GB" + mem_text
    return txt + "\n"


def show_disco_info():
    disco = psutil.disk_usage('.')
    total = round(disco.total / (1024 * 1024 * 1024), 2)
    available = total - round(disco.used / (1024 * 1024 * 1024), 2)
    txt = f"Espaço livre (Total: {str(total)} GB): " + str(available) + "GB"
    return txt

# Todo: mostra info cpu
info_cpu = cpuinfo.get_cpu_info()
def mostra_info_cpu():
    txt = "-*" * 10
    txt += "\n" + mostra_texto( "Nome: ", "brand")
    txt += "\n" + mostra_texto("Arquitetura: ", "arch")
    txt += "\n" + mostra_texto("Palavra (bits): ", "bits")
    txt += "\n" + mostra_texto("Frequência (MHz): ", "freq")
    txt += "\n" + mostra_texto("Núcleos (físicos) : ", "nucleos")
    return txt

# todo: Mostra texto de acordo com uma chave:
def mostra_texto(nome, chave):

    if chave == "freq":
        return nome + str(round(psutil.cpu_freq().current, 2))
    elif chave == "nucleos":
        s = str(psutil.cpu_count())
        s = s + " (" + str(psutil.cpu_count(logical=False)) + ")"
        return nome + s
    else:
        return nome + str(info_cpu[chave])



def show_redes_info():
    txt = '{:>4}'.format("End.")
    txt += '{:>6}'.format("Tipo")
    txt += '{:>20}'.format("Status")
    txt += '{:>30}'.format("Endereço")
    # txt += '{:>40}'.format("Local")
    # txt += '{:<10}'.format("Porta l.")
    txt += '{:>40}'.format("PID")
    # print(txt)
    info = ''
    for i in psutil.net_connections()[0:10]:
        info += '{:>5} {:>4} {:>19} {:>30} {:>40} \n'.format(obtem_nome_familia(i.family), obtem_tipo_socket(i.type), i.status, i.laddr.ip, i.pid)
        # print('{:>5} {:>4} {:>19} {:>30} {:>40}'.format(obtem_nome_familia(i.family), obtem_tipo_socket(i.type), i.status, i.laddr.ip, i.pid))
    return txt + "\n"+ info

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


def get_files_info():
    list = os.listdir('.')
    dictionary = {}
    for i in list:
        if os.path.isfile(i):
            dictionary[i] = []
            dictionary[i].append(os.stat(i).st_size)
            dictionary[i].append(os.stat(i).st_atime)
            dictionary[i].append(os.stat(i).st_mtime)

    txt = '{:11}'.format("Tamanho")
    txt = txt + '{:27}'.format("Data de Modificação")
    txt = txt + '{:27}'.format("Data de Criação")
    txt = txt + 'Nome'
    title = txt

    for i in dictionary:
        kb = dictionary[i][0] / 1000
        size = '{:10}'.format(str('{:.2f}'.format(kb) + 'KB'))
        # print(size, time.ctime(dictionary[i][2]), " ", time.ctime(dictionary[i][1]), " ", i)
        a = size + str(time.ctime(dictionary[i][2])) + "  " * 2 + str(time.ctime(dictionary[i][1])) + " " * 3 + str(i)
        info = '\n' + a
    return title + info


def get_pids():
    try:
        processes = psutil.pids()
        list = []
        for p in processes[1:10]:
            list.append(p)
        info = ''
        for x in list:
            process_list = psutil.Process(x)
            name = process_list.name()
            m = round(process_list.memory_percent(), 2)
            cpu = int(process_list.cpu_percent(interval=1.0))
            info += "\nNome: {:<20}   Pid: {:<10}   Memoria: {:>3}%  CPU: {}".format(name, x, m, cpu)
        return info

    except Exception as NoSuchProcess:
        print(NoSuchProcess)


if __name__ == '__main__':
    main()
