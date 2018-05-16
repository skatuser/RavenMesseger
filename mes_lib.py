import socket
import select
import json
import argparse
import log_setup
import time
import JIM_lib
import threading
from mes_db import ServerDatabaseMod, ClientDatabaseMod

def get_param():

    parser = argparse.ArgumentParser()
    parser.add_argument('--a', help = 'address', default = '127.0.0.1')
    parser.add_argument('--p', help = 'port', default = 7777);
    parser.add_argument('--m', help = 'client mode', default = 'w')
    args = parser.parse_args()
    address = args.a
    port = int(args.p)
    mode = args.m
    return(address, port, mode)

@log_setup.connections_log
def connect_client(sock, clients, database):
    try:
        client_sock, client_addr = sock.accept()
    except OSError as e:
        pass
    else:
        print('request for connection was recieved')
        while True:
            try:
                msg_buf = client_sock.recv(1024)
                msg = json.loads(msg_buf.decode())
                print('----- {} ------'.format(msg))
            except:
                msg = ''
                print('what the fuck')
                pass
            else:
                print('something happening')
                if msg['action'] == 'presence':
                    if msg['user']['account_name'] not in clients.keys():
                        database.add_client(msg['user']['account_name'], '******')
                    client_sock.send(JIM_lib.ServerResponce(code = 200, message = 'connected without errors').__repr__())
                    print('client connected with address {}'.format(client_addr))
                    clients[msg['user']['account_name']] = (client_sock, client_addr)
                    return(0)


def connect_to_database(filename = 'server_db'):
    server_base = ServerDatabaseMod(filename)
    return(server_base)

def get_clients_from_database(server_base):
    clients_list = server_base.get_clients()
    clients_dict = dict.fromkeys(clients_list)
    return(clients_dict)

class Server:

    def __init__(self):

        self.address = get_param()[0]
        self.port = get_param()[1]
        print(self.address, self.port)
        self.sock = socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM, proto = 0)
        self.sock.bind((self.address, self.port))
        self.sock.listen(5)
        self.sock.settimeout(1)
        print(self.sock)

    def server_loop(self):

        database = connect_to_database()

        clients_info = get_clients_from_database(database)
        print('----------')
        print(list(clients_info.keys()))
        print('----------')

        while True:

            connect_client(self.sock, clients_info, database)

            sock_list = [clients_info[client][0] for client in list(clients_info.keys()) if clients_info[client]]

            read = []
            write = []

            try:
                read, write, e = select.select(sock_list, sock_list, [], 0)
            except Exception as e:
                pass

            for sock_r in read:
                try:
                    msg_buf = sock_r.recv(1024)
                    if msg_buf:
                        print('got message')
                        receiver = json.loads(msg_buf.decode())['to']
                        sock_w = clients_info[receiver][0]
                        try:
                            sock_w.send(msg_buf)
                        except:
                            clients.remove(sock_w)
                            continue
                except:
                    clients_list.remove(sock_r)
                    continue

class Client:

    def __init__(self, name):
        self.address = get_param()[0]
        self.port = get_param()[1]
        self.mode = get_param()[2]
        self.name = name
        print(self.address, self.port)
        self.sock = socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM, proto = 0)
        self.sock.connect((self.address, self.port))

    def confirm_connection(self):

        presence_buf = JIM_lib.ClientPresence(username = self.name)
        try:
            self.sock.send(presence_buf.__repr__())
            print('i have sent')
        except:
            print('what the fuck')
        while True:
            ans_buf = self.sock.recv(1024)
            ans = json.loads(ans_buf.decode())
            if ans['responce'] == 200:
                print('connection confirmed')
                return(ans)
            else:
                print(ans['message'])


    def main_loop(self):

        def writer():
            while True:
                receiver = input('Введите логин получателя ')
                text = input('введите сообщение \n')
                msg = JIM_lib.ClientMessage(sender = self.name, destination = receiver, message = text)
                self.sock.send(msg.__repr__()) 

        def reader():
            while True:
                ans_buf = self.sock.recv(1024)
                ans = json.loads(ans_buf.decode())
                print(ans['message'])

        write_thread = threading.Thread(target = writer, name = 'writer_thread')
        read_thread = threading.Thread(target = reader, name = 'reader_thread')

        write_thread.start()
        read_thread.start()

        #if self.mode == 'w':

         #   while True:
#
 #               msg = input('input your message: ')
  #              msg_json = json.dumps(msg)
   #             msg_buf = msg_json.encode()
    #            self.sock.send(msg_buf)

#        elif self.mode == 'r':
#
 #           while True:
#
 #               ans_buf = self.sock.recv(1024)
  #              print()
   #             ans = json.loads(ans_buf.decode())
    #            print(ans)

