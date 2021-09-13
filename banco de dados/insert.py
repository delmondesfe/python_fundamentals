import sqlite3

conn = sqlite3.connect('cafe.db')

cursor = conn.cursor()

sql = """
    insert into ingrediente(nome, descricao,tipo,unidade_medida)
    values ('agua','solvente universal','liquido','ml');

"""

cursor.execute(sql)

conn.commit()

conn.close()