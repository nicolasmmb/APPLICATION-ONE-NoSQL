from jose import jwt, JWTError
from bson.objectid import ObjectId
from datetime import datetime, timedelta
###
from app.configs.config import TokenConfig
from app.schemas.schemas import TokenData
from app.database.database import user_collection

###
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, HTTPBearer


auth_scheme = HTTPBearer()
#auth_scheme = OAuth2PasswordBearer(tokenUrl='/auth/login')

token = HTTPBearer()


def create_token(data: dict):
    encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=int(TokenConfig.get_token_config()['TOKEN_EXPIRE_MINUTES']))
    encode.update({'exp': expire})
    encoded_jwt = jwt.encode(
        encode,
        TokenConfig.get_token_config()['SECRET_KEY'],
        algorithm=TokenConfig.get_token_config()['ALGORITHM']
    )
    return encoded_jwt


def decode_token(token: str, exeption):
    try:
        decode = jwt.decode(
            token,
            TokenConfig.get_token_config()['SECRET_KEY'],
            algorithms=TokenConfig.get_token_config()['ALGORITHM']
        )
        user_id = decode.get('user_id')

        if not id:
            raise exeption

        token_data = TokenData(user_id=user_id)

    except JWTError:
        raise exeption

    except AssertionError as a:
        print(a)

    return token_data


def get_user(token: str = Depends(auth_scheme)):
    exeption = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Unauthorized',
        headers={
            'WWW-Authenticate': 'Bearer',
            "Content-Type": "application/x-www-form-urlencoded"
        }
    )

    token = decode_token(token.credentials, exeption)
    user_id = user_collection.find_one({"_id": ObjectId(token.user_id)})

    if not user_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credentials Error")

    return user_id
