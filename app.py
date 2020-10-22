import pymongo
from pymongo import MongoClient

#MONGODB se conecta a localhost
MONGO_URI = 'mongodb://localhost'

#Client se conecta al host MONGO_URI
client = MongoClient(MONGO_URI)

#Se almacena la base de datos en la variable db
db = client['Diccionario']

#Solo existe una coleccion en esta base de datos la cual es word
collection = db['word']

#INSERT_ONE para insertar un documento en especifico a la base de datos.
collection.insert_one({
    "_id": 1,
    "word": "Que Xopa",
    "meaning": "Saludar"
})

#FIND Para Buscar todos los documentos.
results = collection.find()
for r in results:
    print(r)
    #print(r['name'])

#FIND_ONE Para BUSCAR un documento en especifico.
#result = collection.find_one({"meaning": "Saludar"})
#    print(result)


#DELETE_ONE Para eliminar un documento en especifico.
#DELETE_MANY Para eliminar todos los documentos.
#results = collection.delete_many({"word": "Chantin"})


#UPDATE_ONE Para cambiar un documento en especifico
#collection.update_one({"word": "Xopa"}, {"$set": {"word": "Que Xopa"}})


#Esta variable muestra la cantidad de documentos ingresados en la coleccion
#number_of_words = collection.count_documents({})
#print(number_of_words)