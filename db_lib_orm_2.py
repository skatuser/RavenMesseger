from sqlalchemy import Column, Integer, Unicode, UniqueConstraint, ForeignKey, create_engine

from sqlalchemy.orm import sessionmaker, relationship

from sqlalchemy.ext.declarative import declarative_base

#Здесь мы объявляем баз и таблицы
#Объявляем базу на стороне сервера
ServerBase = declarative_base()

class Clients(ServerBase):

    __tablename__ = 'clients'

    username = Column(Unicode(), primary_key = True)
    password = Column(Unicode())

    check_1 = UniqueConstraint('username')

    def __repr__(self):
        return "Clients<username: {}".format(self.username)

class History(ServerBase):

    __tablename__ = 'history'

    rec_num = Column(Integer(), primary_key = True, autoincrement = True)
    client = Column(Unicode(), ForeignKey('clients.username'))
    enter_time = Column(Unicode())
    address = Column(Unicode())

class AllContacts(ServerBase):

    __tablename__ = 'contacts'

    rec_num = Column(Integer(), primary_key = True, autoincrement = True)
    client = Column(Unicode(), ForeignKey('clients.username'))
    contact = Column(Unicode(), ForeignKey('clients.username'))


#Объявляем базу на стороне клиента
ClientBase = declarative_base()

class ClientContacts(ClientBase):

    __tablename__ = 'contacts'

    c_id = Column(Integer(), primary_key = True, autoincrement = True)
    name = Column(Unicode())

class ClientMessages(ClientBase):

    __tablename__ = 'messages'

    m_id = Column(Integer(), primary_key = True)
    direction = Column(Unicode())
    contact = Column(Integer(), ForeignKey('contacts.c_id'))
    text = Column(Unicode())


#Создаем класс для работы с базой на стороне сервера
class ServerDatabaseMod():

    def __init__(self, filename):
        engine = create_engine('sqlite:///{}.db'.format(filename))
        session = sessionmaker(bind = engine)()


    def create_db():
        answer = input('You are going to delete all info and create new database. Are you sure? Y/N')
        if answer == 'Y':
            metadata = ServerBase.metadata
            metadata.drop_all(engine)
            metadata.create_all(engine)
        else:
            return 0
    
    def add_client(name, password):
        client = Clients(username = name, password = password)
        session.add(client)
        session.commit()

    def del_client(name):
        query = session.query(Clients).filter(Clients.username == name)
        query.delete()
        session.commit()

    def add_history(client, time, address):
        record = History(client = client, enter_time = time, address = address)
        session.add(record)
        session.commit()

    #Удаляет историю за определенный срок
    def del_history(time, basename):
        pass

    def add_contact(client, contact):
        record = AllContacts(client = client, contact = contact)
        session.add(record)
        session.commit()

#Создаем класс для работы с базой на стороне клиента
class ClientDatabaseMod():

    def __init__(self, filename):
        engine = create_engine('sqlite:///{}.db'.format(filename))
        session = sessionmaker(bind = engine)()

    def create_db():
        answer = input('You are going to delete all info and create new database. Are you sure? Y/N')
        if answer == 'Y':
            metadata = ClientBase.metadata
            metadata.drop_all(engine)
            metadata.create_all(engine)
        else:
            return 0

    def add_contact(name):
        contact = ClientContacts(name = name)
        session.add(contact)
        session.commit()

    def add_message(text, contact, direction):
        message = ClientMessages(text = text, contact = contact, direction = direction)
        session.add(message)
        session.commit()

server_database_session = ServerDatabaseMod('test3')

server_database_session.create_db()

server_database_session.add_client(name = 'Patric Melrous', password = '******')