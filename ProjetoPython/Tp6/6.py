import os
import psutil
import time


def Main():
    print("Começando")
    print(os.path.abspath(os.path.join(os.getcwd(), os.pardir)))
    print(get_list())
    print(get_pids())


def get_list():
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
    print(txt)
    for i in dictionary:
        kb = dictionary[i][0] / 1000
        size = '{:10}'.format(str('{:.2f}'.format(kb) + 'KB'))
        print(size, time.ctime(dictionary[i][2]), " ", time.ctime(dictionary[i][1]), " ", i)

    print('\n')


def get_pids():
    try:
        processes = psutil.pids()
        for p in processes[1:10]:
            process_list = psutil.Process(p)
            name = process_list.name()
            m = round(process_list.memory_percent(), 2)
            cpu = int(process_list.cpu_percent(interval=1.0))
            print("Nome: {:<20}   Pid: {:<10}   Memoria: {:>3}%  CPU: {}".format(name, p, m, cpu))
    except Exception as NoSuchProcess:
        print(NoSuchProcess)




if __name__ == '__main__':
    Main()
