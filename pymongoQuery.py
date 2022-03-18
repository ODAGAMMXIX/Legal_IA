# Get the database using the method we defined in pymongo_test_insert file 
from readsNlistsDocuments import get_database

dbname = get_database()

# Create a new collection
collection_name = dbname["user_1_items"]

item_details = collection_name.find()
#for item in item_details:
   
#    print(item)
    
from pandas import DataFrame

# convert the dictionary objects to dataframe
items_df = DataFrame(item_details)

# see the magic
print(items_df)
