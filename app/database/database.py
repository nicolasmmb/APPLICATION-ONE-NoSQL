from pymongo import MongoClient
from app.configs.config import DatabaseConfig


print(DatabaseConfig().get_url_connection())
__conx = MongoClient(DatabaseConfig().get_url_connection())
__db = __conx.pontotel

user_collection = __db["users"]
