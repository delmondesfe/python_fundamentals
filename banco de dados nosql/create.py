import montydb

client = montydb.MontyClient('comercio')

#criar uma collection

db = client.ingrediente

#inserir um novo documento

doc1 = {
    'nome':'cafe',
    'descricao':'grao',
    'tipo':'liquido',
    'unidade_medida':'ml'
    }

doc2 = {
    'nome':'cha',
    'descricao':'erva',
    'tipo':'liquido',
    'unidade_medida':'g'
    }




db.ingrediente.insert_many(doc1,doc2)
