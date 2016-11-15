#! /utils/mongodb.py

from pymongo import MongoClient

mongoDB = MongoClient('localhost:27017')
database = mongoDB.api4shared

def mongo_data_cursor():
    tbldb = database.data
    return tbldb

def mongo_data_insert(dataout):
    tbldb = database.data
    return tbldb.insert_one(dataout)

def mongo_data_get(query):
    tbldb = database.data
    return tbldb.find_one(query)

def mongo_data_update(id, dataout):
    tbldb = database.data
    return tbldb.replace_one({'id': id}, dataout, upsert=True)
