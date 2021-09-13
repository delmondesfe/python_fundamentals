import sqlite3

conn = sqlite3.connect('cafe.db')

cursor = conn.cursor()

sql_create = """
    CREATE TABLE ingrediente(
        id integer primaty key,
        nome text,
        descricao text,
        tipo text,
        unidade_medida text);
"""


sql_drop = """
    drop table ingrediente;
"""


cursor.execute(sql_create)
