import os
import psutil
import time
import socket


def Main():
    print("Começando")
    print(os.path.abspath(os.path.join(os.getcwd(), os.pardir)))
    print(get_files_info())
    print(get_pids())

    # info_redes()

    # io_status = psutil.net_io_counters(pernic=True)
    # nomes = []
    # for i in io_status:
    #     nomes.append(str(i))
    # for j in nomes:
    #     print(j)
    #     print("\t"+str(io_status[j]))
    # for i in range(4):
    #     time.sleep(1)
    #     io_status = psutil.net_io_counters(pernic=True)
    # for j in nomes:
    #     print(j)
    #     print("\t"+str(io_status[j]))
    # for i in psutil.net_connections():
    #     print(i)


def get_files_teste():
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
    print(txt)
    for i in dictionary:
        kb = dictionary[i][0] / 1000
        size = '{:10}'.format(str('{:.2f}'.format(kb) + 'KB'))
        print(size, time.ctime(dictionary[i][2]), " ", time.ctime(dictionary[i][1]), " ", i)

    print('\n\n')
    print('------------------------***********************------------------------')


def get_pids():
    try:
        processes = psutil.pids()
        list = []
        for p in processes[1:10]:
            list.append(p)

        for x in list:
            process_list = psutil.Process(x)
            name = process_list.name()
            m = round(process_list.memory_percent(), 2)
            cpu = int(process_list.cpu_percent(interval=1.0))
            print("Nome: {:<20}   Pid: {:<10}   Memoria: {:>3}%  CPU: {}".format(name, x, m, cpu))


    except Exception as NoSuchProcess:
        print(NoSuchProcess)
    print('\n\n')
    print('------------------------***********************------------------------')


#
# def info_redes():
#     processes = psutil.pids()
#     processes_list = []
#     for p in processes:
#         x = psutil.Process(p)
#         processes_list.append(x)
#     for conn in processes_list:
#         conn = p.connections()
#     for c in conn:
#         print(str(c))



if __name__ == '__main__':
    Main()
