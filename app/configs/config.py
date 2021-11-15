from dotenv import load_dotenv
import os

load_dotenv()


class DatabaseConfig:
    def __init__(self):
        self.__type_db = 'mongodb://'
        self.__username = os.getenv('MONGO_USERNAME')
        self.__password = os.getenv('MONGO_PASSWORD')
        self.__host = os.getenv("MONGO_HOST")
        self.__port = os.getenv("MONGO_PORT")
        self.__string_db = self.__type_db + self.__username + ':' + self.__password + '@' + self.__host + ':' + self.__port + '/'

    def get_url_connection(self) -> str:
        return self.__string_db


class TokenConfig:
    @staticmethod
    def get_token_config() -> dict:
        return {
            'SECRET_KEY': os.getenv('SECRET_KEY'),
            'ALGORITHM': os.getenv('ALGORITHM'),
            'TOKEN_EXPIRE_MINUTES': os.getenv('TOKEN_EXPIRE_MINUTES')
        }
