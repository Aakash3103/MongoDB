import pymongo

client = pymongo.MongoClient("mongodb+srv://root:Passw0rd@aakash.uf2zk.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name" : "aakash",
    "Email" : "aakash@gmail.com",
    "surname" :"gupta"
}

db1 = client['MongoTest']
coll = db1['test']
coll.insert_one(d)