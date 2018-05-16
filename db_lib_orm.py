from sqlalchemy import Column, Integer, Unicode, UniqueConstraint, ForeignKey, create_engine

from sqlalchemy.orm import sessionmaker, relationship

from sqlalchemy.ext.declarative import declarative_base

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


class ServerDatabaseMod():

    def __init__(self)



def create_server_db(filename):
    answer = input('You are going to delet all info and create new database. Are you sure? Y/N')
    if answer == 'Y':
        metadata = ServerBase.metadata
        engine = create_engine('sqlite:///{}.db'.format(filename))
        metadata.drop_all(engine)
        metadata.create_all(engine)
    else:
        return 0


def create_client_db(filename):
    answer = input('You are going to delet all info and create new database. Are you sure? Y/N')
    if answer == 'Y':
        metadata = ClientBase.metadata
        engine = create_engine('sqlite:///{}.db'.format(filename))
        metadata.drop_all(engine)
        metadata.create_all(engine)
    else:
        return 0

def add_client(name, password, basename):
    client = Clients(username = name, password = password)
    engine = create_engine('sqlite:///{}.db'.format(basename))
    session = sessionmaker(bind = engine)()
    session.add(client)
    session.commit()

def del_client(name, basename):
    engine = create_engine('sqlite:///{}.db'.format(basename))
    session = sessionmaker(bind = engine)()
    query = session.query(Clients).filter(Clients.username == name)
    query.delete()
    session.commit()

def add_history(client, time, address, basename):
    record = History(client = client, enter_time = time, address = address)
    engine = create_engine('sqlite:///{}.db'.format(basename))
    session = sessionmaker(bind = engine)()
    session.add(record)
    session.commit()

#Удаляет историю за определенный срок
def del_history(time, basename):
    pass
    
def server_add_contact(client, contact, basename):
    record = AllContacts(client = client, contact = contact)
    engine = create_engine('sqlite:///{}.db'.format(basename))
    session = sessionmaker(bind = engine)()
    session.add(record)
    session.commit()

def client_add_contact(name, basename)





#add_client('Jack Bower', ';lamcpvom,d/', 'test2')
#add_client('Jameson Born', 'Threadstone', 'test2')

add_history('fgssdg', 'fagaer', 'sdrg', 'test2')
add_history('fgarvdfsg', 'fvdvf', 'tryue', 'test2')



#create_server_db('test2')
#engine = create_engine('sqlite:///test2.db')
#session = sessionmaker(bind = engine)()
#user_1 = Clients(username = 'John Smith', password = '******')
#session.add(user_1)
#session.commit()