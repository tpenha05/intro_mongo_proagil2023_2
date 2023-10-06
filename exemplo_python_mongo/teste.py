import pymongo 

client_con = pymongo.MongoClient('mongodb+srv://admin:admin@cluster0.9joj4ma.mongodb.net/?retryWrites=true&w=majority')

pacientes_col = client_con["Pacientes"]["Pacientes"]

filter = {
    "idade" : 43
}

projection = {
    "_id" : 0,
    "nome_paciente" : 1
}

resultados = list(pacientes_col.find(filter,projection))

print('Todos os pacientes')
print(resultados)
