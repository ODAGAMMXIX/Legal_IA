def get_database():
    from pymongo import MongoClient
    import pymongo

   
    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    from pymongo import MongoClient
    client = MongoClient('localhost', 27017)

    # Create the database for our example (we will use the same database throughout the tutorial
    return client['user_shopping_list']

dbname = get_database()



from dateutil import parser
expiry_date = '2021-07-13T00:00:00.000Z'
expiry = parser.parse(expiry_date)

collection_name = dbname["user_1_items"]
item_3 = {
                    "item_name" : "Bread",
                    "quantity" : 2,
                    "ingredients" : "all-purpose flour",
                    "expiry_date" : expiry
        }
collection_name.insert_one(item_3)