from pymongo import MongoClient
from fbelib.config import settings

__author__ = 'Regis FLORET'

Client = MongoClient(settings.ServerAddress, settings.ServerPort)
Db = Client[settings.DatabaseName]






