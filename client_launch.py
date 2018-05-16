import mes_lib

name = input('input name ')

client = mes_lib.Client(name = name)

confirmation = client.confirm_connection()

print(confirmation)

client.main_loop()