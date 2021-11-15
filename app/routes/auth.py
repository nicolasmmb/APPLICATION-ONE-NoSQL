from fastapi import APIRouter, Depends, status, HTTPException, Response
###
from app.database.database import user_collection
from app.schemas import schemas
from app.utils import utils
###
import time
from app.utils import oauth

router = APIRouter(tags=['Authentication'])


@router.post('/login')
async def login(user_credentials: schemas.UserLogin):

    if not user_credentials:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials")

    if not user_credentials.senha:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Invalid Password')

    if not user_credentials.cpf:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Invalid CPF')

    user = user_collection.find_one({"cpf": utils.Validator.only_number(user_credentials.cpf)})

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User Not Found")

    if not utils.verify(user_credentials.senha, user["senha"]):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials")

    auth = oauth.create_token({"user_id": str(user["_id"])})

    return {
        "token": auth,
        "type": 'bearer'
    }
