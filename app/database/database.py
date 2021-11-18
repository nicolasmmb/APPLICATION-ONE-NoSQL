from pymongo import MongoClient
from app.configs.config import DatabaseConfig


__conx = MongoClient(DatabaseConfig.get_url_connection())
__db = __conx.pontotel

user_collection = __db["users"]
user_collection.create_index("email", unique=True)
user_collection.create_index("cpf", unique=True)
user_collection.create_index("pis", unique=True)
