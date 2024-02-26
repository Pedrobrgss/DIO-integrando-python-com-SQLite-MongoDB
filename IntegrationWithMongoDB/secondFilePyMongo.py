import pprint
from IntegrationWithMongoDB.pyMongoApplication import client, banks

# Cria o banco de dados
db = client.test

for post in banks.find():
    pprint.pprint(post)
