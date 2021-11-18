from dotenv import load_dotenv
import os

load_dotenv()


class DatabaseConfig:
    @staticmethod
    def get_url_connection() -> str:
        if os.getenv('MONGO_USE_SRV') == 'True' or os.getenv('MONGO_USE_SRV') == 'true' or os.getenv('MONGO_USE_SRV') == None:
            print('MONGO_USE_SRV: TRUE')
            __type_db = 'mongodb+srv://'
            __username = os.getenv('MONGO_USERNAME')
            __password = os.getenv('MONGO_PASSWORD')
            __host = os.getenv("MONGO_HOST")
            __port = os.getenv("MONGO_PORT")
            __string_db = __type_db + __username + ':' + __password + '@' + __host + '/'
            return __string_db
        else:
            print('MONGO_USE_SRV: FALSE')
            __type_db = 'mongodb://'
            __username = os.getenv('MONGO_USERNAME')
            __password = os.getenv('MONGO_PASSWORD')
            __host = os.getenv("MONGO_HOST")
            __port = os.getenv("MONGO_PORT")
            __string_db = __type_db + __username + ':' + __password + '@' + __host + ':' + __port + '/'
            return __string_db

    # @staticmethod
    # def get_url_connection_srv() -> str:
    #     __type_db = 'mongodb+srv://'
    #     __username = os.getenv('MONGO_USERNAME')
    #     __password = os.getenv('MONGO_PASSWORD')
    #     __host = os.getenv("MONGO_HOST")
    #     __port = os.getenv("MONGO_PORT")
    #     __string_db = __type_db + __username + ':' + __password + '@' + __host + '/'
    #     return __string_db


class TokenConfig:
    @staticmethod
    def get_token_config() -> dict:
        return {
            'SECRET_KEY': os.getenv('SECRET_KEY'),
            'ALGORITHM': os.getenv('ALGORITHM'),
            'TOKEN_EXPIRE_MINUTES': os.getenv('TOKEN_EXPIRE_MINUTES')
        }
