import pymongo as pyM

client = pyM.MongoClient("mongodb+srv://pymongo:Pedro12272@cluster0.cmbmf5b.mongodb.net/?retryWrites=true&w=majority"
                         "&appName=Cluster0")
db = client.test
collection = db.test_collection
print(db.test_collection)

bank = [{
    "nome": "Pedro",
    "cpf": "123.456.789-09",
    "endereco": "Samambaia Sul",
    "tipo_conta": "Conta corrente",
    "agencia": "0007",
    "numero  da conta": "26342-1"},
    {
    "nome": "Amanda",
    "cpf": "987.654.321-09",
    "endereco": "Asa Sul",
    "tipo_conta": "Conta poupança",
    "agencia": "0003",
    "numero da conta": "12345-1/500"},
    {
    "nome": "Lucas",
    "cpf": "341.634.312-08",
    "endereco": "Taguatinga",
    "tipo_conta": "Conta corrente",
    "agencia": "0004",
    "numero da conta": "72365-1/"
    }
]

banks = db.banks
result = banks.insert_many(bank)
