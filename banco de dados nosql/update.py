import montydb

client = montydb.MontyClient('cafe')

db = client.ingrediente

db.ingrediente.update_one({'nome':'cafe'},{'$set': {'unidade_medida':'kg'}})