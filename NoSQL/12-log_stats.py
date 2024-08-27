#!/usr/bin/env python3
'''
Provide stats about Nginx logs stored in MongoDB
'''
from pymongo import MongoClient

def log_stats():
    x = MongoClient('mongodb://localhost:27017').logs.nginx


    print(f'{x.count_documents({})} logs')

 
    print('Methods:')
    print(f'\tmethod GET: {x.count_documents({"method": "GET"})}')
    print(f'\tmethod POST: {x.count_documents({"method": "POST"})}')
    print(f'\tmethod PUT: {x.count_documents({"method": "PUT"})}')
    print(f'\tmethod PATCH: {x.count_documents({"method": "PATCH"})}')
    print(f'\tmethod DELETE: {x.count_documents({"method": "DELETE"})}')


    print(f'{x.count_documents({"method": "GET", "path": "/status"})} status check')

if __name__ == "__main__":
    log_stats()
