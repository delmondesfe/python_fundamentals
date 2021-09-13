import sqlite3
from typing import Counter

conn = sqlite3.connect('cafe.db')

cursor = conn.cursor()

sql = """update ingrediente set unidade_medida = 'l' where id = 1 ;"""

cursor.execute(sql)

conn.commit()