from pymongo import MongoClient
from app.configs.config import DatabaseConfig


__conx = MongoClient(DatabaseConfig.get_url_connection_srv())
__db = __conx.pontotel

user_collection = __db["users"]
