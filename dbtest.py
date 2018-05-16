from mes_db import ServerDatabaseMod

server_database = ServerDatabaseMod('server_db')

server_database.add_client('John', '******')

server_database.add_client('Steve', '******')

server_database.add_client('Richard', '******')

client = server_database.get_client_by_name('John')

clients = server_database.get_clients()

print(client)

print('------------')

print(clients)