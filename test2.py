import pymongo

client = pymongo.MongoClient("mongodb+srv://tushar_v04:SOq8oZMKiwPeYBXo@cluster0.pju1d.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")#plz use your own database connection string
db=client['test']
collections=db['test1']
dic={'name':'Tushar verma','Age':20}
collections.insert_one(dic)