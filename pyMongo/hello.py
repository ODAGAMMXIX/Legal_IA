# Check the versions of Linux Python, its libraries, MongoDB, VSCode extentions etc.
# import the complete PyMongo library and check its version
import pymongo
print ("pymongo version:", pymongo.version)

from pymongo import MongoClient # import the MongoClient class

mongo_client = MongoClient('localhost', 27017) # Gets useful data 4 MongoDB

host_info = mongo_client['HOST']  #Show config
print ("\nhost:", host_info)