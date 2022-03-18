#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# import the complete PyMongo library and check its version
import pymongo
print ("pymongo version:", pymongo.version)

# import the MongoClient class
from pymongo import MongoClient

# build a new client instance for MongoDB passing
# the string domain and integer port to the host parameters
mongo_client = MongoClient('localhost', 27017)

host_info = mongo_client['HOST']
print ("\nhost:", host_info)