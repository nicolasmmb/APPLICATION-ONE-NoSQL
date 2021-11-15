from pydantic import BaseModel
from typing import Optional
from app.utils.utils import hash, remove_none


### ADDRESS ###
class AddressBase(BaseModel):
    pais: Optional[str] = None
    estado: Optional[str] = None
    municipio: Optional[str] = None
    cep: Optional[str] = None
    rua: Optional[str] = None
    numero: Optional[int] = None
    complemento: Optional[str] = None

    def __getitem__(self, key):
        return self.__dict__[key]

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    class Config:
        orm_mode = True


class AddressUpdate(BaseModel):
    pais: str
    estado: str
    municipio: str
    cep: str
    rua: str
    numero: int
    complemento: str

    def __getitem__(self, key):
        return self.__dict__[key]

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    _id: Optional[str] = None
    nome: Optional[str] = None
    email: Optional[str] = None
    cpf: Optional[str] = None
    pis: Optional[str] = None
    senha: Optional[str] = None
    endereco: Optional[AddressBase] = None

    def __getitem__(self, key):
        return self.__dict__[key]

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def hash_password(self):
        self.senha = hash(self.senha)

    class Config:
        orm_mode = True


class UserUpdate(BaseModel):
    _id: str
    nome: str
    email: str
    cpf: str
    pis: str
    senha: str
    endereco: AddressUpdate

    def __getitem__(self, key):
        return self.__dict__[key]

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def hash_password(self):
        self.senha = hash(self.senha)

    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    cpf: str
    senha: str

    def __getitem__(self, key):
        return self.__dict__[key]

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    class Config:
        orm_mode = True


class Token(BaseModel):
    token: str
    type: str

    def __getitem__(self, key):
        return self.__dict__[key]

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    class Config:
        orm_mode = True


class TokenData(BaseModel):
    user_id: Optional[str] = None

    def __getitem__(self, key):
        return self.__dict__[key]

    def __setitem__(self, key, value):
        self.__dict__[key] = value


def userEntity(item) -> dict:
    # exclude none values
    values = {k: v for k, v in item.items()}
    values['_id'] = str(values['_id'])

    return values
    # items = remove_none(item)
    # try:
    #     items['_id'] = str(item['_id'])
    # except:
    #     print('userEntity: _id not found')
    #     pass
    # return items


def userEntityList(item) -> list:
    return[userEntity(user) for user in item]


# class UserUpdate(BaseModel):
#     nome: Optional[str] = None
#     email: Optional[str] = None
#     cpf: Optional[str] = None
#     pis: Optional[str] = None
#     senha: Optional[str] = None

#     def __getitem__(self, key):
#         return self.__dict__[key]

#     def __setitem__(self, key, value):
#         self.__dict__[key] = value

#     class Config:
#         orm_mode = True


# class UserGet(BaseModel):
#     id: int
#     nome: str
#     email: str
#     cpf: str
#     pis: str
#     senha: str

#     def __getitem__(self, key):
#         return self.__dict__[key]

#     def __setitem__(self, key, value):
#         self.__dict__[key] = value

#     class Config:
#         orm_mode = True


# class AddressUpdate(BaseModel):
#     pais: Optional[str] = None
#     estado: Optional[str] = None
#     municipio: Optional[str] = None
#     cep: Optional[str] = None
#     rua: Optional[str] = None
#     numero: Optional[int] = None
#     complemento: Optional[str] = None
#     user_id: Optional[int] = None

#     def __getitem__(self, key):
#         return self.__dict__[key]

#     def __setitem__(self, key, value):
#         self.__dict__[key] = value

#     class Config:
#         orm_mode = True


# class AddressGet(BaseModel):
#     id: int
#     pais: str
#     estado: str
#     municipio: str
#     cep: str
#     rua: str
#     numero: int
#     complemento: str
#     #user_id: Optional[int]

#     def __getitem__(self, key):
#         return self.__dict__[key]

#     def __setitem__(self, key, value):
#         self.__dict__[key] = value

#     class Config:
#         orm_mode = True
