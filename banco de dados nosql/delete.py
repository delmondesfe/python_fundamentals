import montydb

client = montydb.MontyClient('cafe')

db = client.ingrediente

db.ingrediente.delete_one({'nome':'cafe'})

for documento in db.ingrediente.find():
    print(documento)