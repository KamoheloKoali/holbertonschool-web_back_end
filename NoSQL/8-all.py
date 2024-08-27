#!/usr/bin/env python3
"""
8-all.py
Contains the `list_all` function that lists all documents in a MongoDB collection.
"""

def list_all(mongo_collection):
    """
    Lists all documents in a collection.
    If the collection is empty, it returns an empty list.
    
    Parameters:
    - mongo_collection: The pymongo collection object.

    Returns:
    - A list of documents.
    """
    return list(mongo_collection.find())

