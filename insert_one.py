def get_database():
    from pymongo import MongoClient
    import pymongo
    
    from pymongo import MongoClient # Creates a connection
    client = MongoClient('localhost', 27017)
   
    return client['user_shopping_list'] # Creates the database

dbname = get_database()

from dateutil import parser
expiry_date = '2023-03-18T00:00:00.000Z'
expiry = parser.parse(expiry_date) # Splits date from time

collection_name = dbname["user_1_items"] #Inserts nan item into my collection 
item_4 = {
                    "item_name" : "WashingPowder",
                    "quantity" : 12,
                    "ingredients" : "Lots_of_Chemicals",
                    "expiry_date" : expiry
        }
collection_name.insert_one(item_4)