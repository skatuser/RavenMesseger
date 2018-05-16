from db_lib import *

database = ServerDatabase('testbase.db')

database.create_tables_from_scratch()

database.add_client('lol', 'etoparol')

database.add_client('hgfsgdfk', '769hcwdkjhf9')

clients = database.get_clients()

clients_2 = []

for i in range(len(clients)):
	client = clients[i][0]
	clients_2.append(client)


print(clients)

print(clients_2)