from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from bson.objectid import ObjectId
#
from app.schemas import schemas
from app.database.database import user_collection
# Utils
from app.utils import utils
from app.utils import oauth


router = APIRouter(
    prefix="/users",
    # tags=['USERS']
)


@router.post('/create', status_code=status.HTTP_201_CREATED, tags=['USERS'])
async def create_user(user: schemas.UserBase):
    if user is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No Data Found")

    if not utils.Validator.validateCPF(cpf=user.cpf):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="CPF Is Not Valid")

    if not utils.Validator.validatePIS(pis=user.pis):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="PIS Is Not Valid")

    try:

        user.cpf = utils.Validator.only_number(user.cpf)
        user.pis = utils.Validator.only_number(user.pis)
        user.hash_password()

        user_return = user_collection.insert_one(user.dict())

        if user_return is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User Not Created")

        return_data = {
            'response': str(user_return.inserted_id),
            'message': 'User created'
        }

        return return_data

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e.__cause__))


@router.get('/get-all/', status_code=status.HTTP_200_OK, tags=['USERS'])
async def get_users(limit: int = None, user_data: any = Depends(oauth.get_user)):

    try:
        if limit:
            users = user_collection.find().limit(limit)
        else:
            users = user_collection.find()

        return_data = {
            'response': schemas.userEntityList(users),
            'message': 'Get all users'
        }

        return return_data

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e.__cause__))


@router.get('/get-by-id/{id}', status_code=status.HTTP_200_OK, tags=['USERS'])
async def get_user_by_id(id: str, user_data: any = Depends(oauth.get_user)):

    if ObjectId().is_valid(id) != True:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid Id")

    user = user_collection.find_one({'_id': ObjectId(id)})

    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User Not Found")

    return_data = {
        'response': schemas.userEntity(user),
        'message': 'User found'
    }

    return return_data


@router.get('/get-my-info',  status_code=status.HTTP_200_OK, tags=['USER-AUTO'])
async def get_my_user(user_data: any = Depends(oauth.get_user)):

    user = user_collection.find_one({'_id': ObjectId(user_data['_id'])})
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User Not Found")

    return_data = {
        'response': schemas.userEntity(user),
        'message': 'User found'
    }
    return return_data


@router.put('/update/{id}', status_code=status.HTTP_200_OK, tags=['USERS'])
async def update_user_by_id(id: str, user: schemas.UserUpdate, user_data: any = Depends(oauth.get_user)):
    if ObjectId().is_valid(id) != True:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid Id")

    if not utils.ValidateCPF(cpf=user.cpf).validate():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="CPF Is Not Valid")

    if not utils.ValidatePIS(pis=user.pis).validate():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="PIS Is Not Valid")

    user.cpf = utils.Validator.only_number(user.cpf)
    user.pis = utils.Validator.only_number(user.pis)

    user.hash_password()
    user_resp = user_collection.find_one_and_update(
        {'_id': ObjectId(id)},
        {"$set": user.dict()},
    )

    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User Not Found")

    return_data = {
        'response': schemas.userEntity(user_collection.find_one({'_id': ObjectId(id)})),
        'message': 'User Updated'
    }

    return return_data


@router.put('/update-my-user', status_code=status.HTTP_200_OK, tags=['USER-AUTO'])
async def update_my_user(user: schemas.UserUpdate, user_data: any = Depends(oauth.get_user)):

    if ObjectId().is_valid(user_data['_id']) != True:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid Id")

    if not utils.ValidateCPF(cpf=user.cpf).validate():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="CPF Is Not Valid")

    if not utils.ValidatePIS(pis=user.pis).validate():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="PIS Is Not Valid")

    user.cpf = utils.Validator.only_number(user.cpf)
    user.pis = utils.Validator.only_number(user.pis)

    user.hash_password()
    user_resp = user_collection.find_one_and_update(
        {'_id': ObjectId(user_data['_id'])},
        {"$set": user.dict()},
    )

    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User Not Found")

    return_data = {
        'response': schemas.userEntity(user_collection.find_one({'_id': ObjectId(user_data['_id'])})),
        'message': 'User Updated'
    }

    return return_data


@router.delete('/delete/{id}', status_code=status.HTTP_200_OK, tags=['USERS'])
async def delete_user_by_id(id: str, user_data: any = Depends(oauth.get_user)):

    if ObjectId().is_valid(id) != True:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid Id")

    user = user_collection.find_one_and_delete({'_id': ObjectId(id)})

    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User Not Deleted")

    return_data = {
        'response': schemas.userEntity(user),
        'message': 'User Deleted'
    }

    return return_data


@router.delete('/delete-my-user', status_code=status.HTTP_200_OK, tags=['USER-AUTO'])
async def delete_my_user(user_data: any = Depends(oauth.get_user)):

    if ObjectId().is_valid(user_data['_id']) != True:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid Id")

    user = user_collection.find_one_and_delete({'_id': ObjectId(user_data['_id'])})

    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User Not Deleted")

    return_data = {
        'response': schemas.userEntity(user),
        'message': 'User Deleted'
    }

    return return_data
