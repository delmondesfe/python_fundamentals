import sqlite3

conn = sqlite3.connect('cafe.db')

cursor = conn.cursor()

sql_select = "select * from ingrediente"

for registro in cursor.execute(sql_select):
    print('ID: ',registro[0])
    print('nome: ' ,registro[1])
    print('Descrição: ',registro[2])
    print('Tipo: ',registro[3])
    print('Unidade de Medida: ',registro[4])

conn.close()