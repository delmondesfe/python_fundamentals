import montydb

client = montydb.MontyClient('cafe')

db = client.ingrediente

for documento in db.ingrediente.find():
    print(documento)