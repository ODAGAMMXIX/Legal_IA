def get_database():
    from pymongo import MongoClient
    import pymongo
    
    from pymongo import MongoClient 
    client = MongoClient('localhost', 27017) # Gets useful data 4 MongoDB

    return client['user_shopping_list'] 

if __name__ == "__main__":    # Object
    
    dbname = get_database()
    collection_name = dbname["user_1_items"]
    item_5 = {                              # Insets an Item
                "_id" : "U1IT00003",
                "item_name" : "DishWashe",
                "max_discount" : "10%",
                "batch_number" : "WR450020FRG",
                "price" : 400,
                "category" : "kitchen appliance + LifeSaver"
                }

    item_6 = {                              # Insets another Item
                "_id" : "U1IT00004",
                "item_name" : "Olive Oil",
                "category" : "food",
                "quantity" : 2,
                "price" : 9,
                "item_description" : "Italian D.O.C."
                }
    collection_name.insert_many([item_5,item_6])
    