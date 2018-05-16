import sqlite3 as sql
import os

#База данных на стороне сервера
class ServerDatabase:

    def __init__(self, filename = 'server_base.db'):
        self.filename = filename
        if self.filename in os.listdir():
            self.existance_mark = True
        else:
            self.existance_mark = False
        self.conn = sql.connect(self.filename)

    def create_tables_from_scratch(self):
        if self.existance_mark:
            answer = input('Server database have been already created. Do you want to drop it and make new one? Y/N')
            if answer == 'N':
                return None
            else:
                self.cursor = self.conn.cursor()
                self.cursor.execute("""drop table if exists clients""")
                self.cursor.execute("""drop table if exists history""")
                self.cursor.execute("""drop table if exists contacts""")
                self.conn.commit()
        else:

            self.cursor = self.conn.cursor()

        self.cursor.execute("""create table clients
        (
            username text primary key,
            password text
        )""")

        self.cursor.execute("""create table history
        (
            client text references clients (username),
            enter_time text,
            address text
        )""")

        self.cursor.execute("""create table contacts
        (
            client text references clients (username),
            contact text references clients (username)
        )""")

        self.conn.commit()      

    def add_client(self, username, password):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""insert 
            into clients
            (username, password)
            values
            ('{0}', '{1}')""".format(username, password))
        self.conn.commit()

    def add_history(self, username, time, address):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""insert 
            into history
            (username, enter_time, address)
            values
            ('{0}', '{1}', '{2}')""".format(username, time, address))
        self.conn.commit()

    def add_contacts(self, username, contact):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""insert 
            into contacts
            (username, contact)
            values
            ('{0}', '{1}',)""".format(username, contact))
        self.conn.commit()

    def del_contact(self, username, contact):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""delete 
            from contacts where contact = {0} and username = {1}""".format(contact, username))
        self.conn.commit()

    def get_clients(self):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""select username from clients""")
        clients = self.cursor.fetchall()
        self.conn.commit()
        clients_list = []
        for i in range(len(clients)):
            client = clients[i][0]
            clients_list.append(client)
        return(clients_list)



#База данных на стороне клиента
class ClientDatabase:

    def __init__(self, filename = 'client_base.db'):
        self.filename = filename
        if self.filename in os.listdir():
            self.existance_mark = True
        else:
            self.existance_mark = False
        self.conn = sql.connect(self.filename)

    def create_tables_from_scratch(self):
        if self.existance_mark:
            answer = input('Server database have been already created. Do you want to drop it and make new one? Y/N')
            if answer == 'N':
                return None
            else:
                self.cursor = self.conn.cursor()
                self.cursor.execute("""drop table if exists contacts""")
                self.cursor.execute("""drop table if exists messages""")
                self.conn.commit()
        else:
            self.cursor = self.conn.cursor()


        #Первая таблица - список контактов
        self.cursor.execute("""create table contacts
        (
            name text primary key,
        )""")
        #Вторая таблица - сообщение, ссылка на контакт, текст, направление(входящее или исходящее)
        self.cursor.execute("""create table messages
        (
            contact text references contactss (name),
            message_text text, 
            direction text 
        )""")
    
    def add_contact(self, name):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""insert 
            into contacts
            (name)
            values
            ('{}')""".format(username, name))
        self.conn.commit()

    def add_message(self, name, text, direction):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""insert 
            into messages
            (name, message_text, direction)
            values
            ('{0}', '{1}', '{2}')""".format(name, text, direction))
        self.conn.commit()    