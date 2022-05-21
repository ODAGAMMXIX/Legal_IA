import pymongo
from apriori_2_algorithm import apriori_2

def fillDatabase(application_collection):
    action_data = {'type': 'ACAO' , 'itemset': ['acao','nexo','dano'],
                   'data': [['acao'],['acao','nexo'],['acao', 'nexo', 'dano'],['acao', 'nexo', 'dano'],['acao', 'nexo', 'dano'],['acao', 'nexo', 'dano'],['acao', 'nexo', 'dano'],['acao', 'nexo', 'dano'],['acao', 'nexo', 'dano'],['acao', 'nexo', 'dano'],['nexo', 'acao', 'dano'],['acao', 'dano'],['acao', 'nexo'],['acao', 'nexo', 'dano'],['acao', 'nexo', 'dano'],['acao', 'nexo', 'dano'],['acao', 'nexo', 'dano'],['acao', 'nexo', 'dano'],['nexo', 'acao', 'dano'],['acao', 'nexo', 'dano'],['acao', 'nexo', 'dano'],['nexo', 'acao', 'dano'],['acao', 'nexo', 'dano'],['acao'],['acao','nexo'],['acao', 'nexo', 'dano'],['acao', 'nexo', 'dano'],['nexo', 'acao', 'dano'], ['acao', 'nexo', 'dano'],['nexo', 'acao', 'dano']]
                }
    application_collection.insert_one(action_data)

    omission_data = {'type': 'OMISSAO', 'itemset': ['omissao','nexo','dano'], 
                     'data': [['omissao'],['omissao', 'nexo'],['omissao', 'nexo', 'dano'],['nexo', 'omissao', 'dano'],['omissao', 'dano'],['omissao', 'dano', 'nexo'],['omissao', 'dano', 'nexo'],['omissao', 'dano', 'nexo'],['omissao', 'dano', 'nexo'],['omissao', 'dano', 'nexo'],['dano', 'omissao'],['omissao', 'dano', 'nexo'],['nexo', 'omissao', 'dano'],['omissao', 'dano', 'nexo'],['omissao', 'dano', 'nexo'],['omissao', 'dano', 'nexo'],['omissao', 'dano', 'nexo'],['omissao', 'dano', 'nexo'],['omissao', 'dano', 'nexo'],['omissao', 'nexo', 'dano'],['nexo', 'omissao', 'dano'],['omissao', 'nexo', 'dano'],['omissao'],['omissao', 'nexo'],['omissao', 'nexo', 'dano'],['omissao', 'nexo', 'dano']]
                     }
    application_collection.insert_one(omission_data)                     


def create_connection():
    application_client = pymongo.MongoClient("mongodb://localhost:27017/")
    application_db = application_client["ia"]
    application_collection = application_db["apriori"]
    return application_collection

def createSet(data): # Mongo array 2 Python set
    set_list = []
    for item in data:
        item_set = set(item)
        set_list.append(item_set)
    return set_list
    
def main():
    application_collection = create_connection()
    fillDatabase(application_collection)

    base_data = application_collection.find()
    
    for item_data in base_data:
        transaction = createSet(item_data["data"])
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print(f'processing SET {item_data["type"]}')
        result = apriori_2(item_data["itemset"], transaction, 0.4, 0.5) # parameters 
        print("+===============================")
        print(f"result {result}")

    application_collection.drop()



main()






    