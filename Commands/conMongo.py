from pymongo import MongoClient

Client = MongoClient()
db = Client["Library"]
collection = db["Books"]
book = {}
book ["title"] = "Mongodb Guide"
book ["year"] = 2015
book ["Author"] = "Aditya"
collection.insert(book)

print(book)
print(book["Author"])
