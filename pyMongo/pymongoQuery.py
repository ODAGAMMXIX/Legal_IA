from InsertAcouple import get_database # Method from another test

dbname = get_database()

collection_name = dbname["user_1_items"] # My collection

item_details = collection_name.find() #My Finding Method 
    
from pandas import DataFrame

items_df = DataFrame(item_details) # vis-a-vis .pretty()

print(items_df)
