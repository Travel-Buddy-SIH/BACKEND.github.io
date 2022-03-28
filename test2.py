import pymongo
from flask import Flask
from flask_cors import CORS
app =Flask(__name__)
CORS(app)
client = pymongo.MongoClient("mongodb+srv://tushar_v04:SOq8oZMKiwPeYBXo@cluster0.pju1d.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client['test']
collection1 = db['Places']
@app.route('/place')
def Places():
    findAll1 = collection1.find({},{'_id':0})
    list1 = []
    for i in findAll1:
        list1.append(i)
    return({"Data of Places":list1})

collection2 = db['Market']
@app.route('/market')
def Markets():
    findAll2 = collection2.find({}, {'_id': 0})
    list2 = []
    for i in findAll2:
        list2.append(i)
    return ({"Data of Market": list2})


collection3 = db['Restaurants']
@app.route('/restaurant')
def Restaurant():
    findAll3 = collection3.find({}, {'_id': 0})
    list3 = []
    for i in findAll3:
        list3.append(i)
    return ({"Data of Restaurant": list3})


collection4 = db['Hotels']
@app.route('/hotel')
def Hotels():
    findAll4 = collection4.find({}, {'_id': 0})
    list4 = []
    for i in findAll4:
        list4.append(i)
    return ({"Data of Hotels": list4})

if __name__ == "__main__":
    app.run(debug=True)