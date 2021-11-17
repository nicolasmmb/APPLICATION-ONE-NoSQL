from fastapi import FastAPI
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200


def return_token() -> str:
    model_body = {
        "cpf": "38040291593",
        "senha": "senha"
    }

    response = client.post("/auth/login", json=model_body)
    token_auth = response.json().get("token")

    return token_auth


# def test_create_user():
#     model_body = {
#         "nome": "Test User",
#         "email": "user@test.com",
#         "cpf": "38040291593",
#         "pis": "003.57651.58-8",
#         "senha": "senha"
#     }

#     response = client.post("/api/users/create", json=model_body)
#     assert response.status_code == 201 or 400


# def test_get_token():
#     model_body = {
#         "cpf": "38040291593",
#         "senha": "senha"
#     }

#     response = client.post("/auth/login", json=model_body)
#     token_auth = response.json().get("token")

#     assert response.status_code == 200


# def test_users_get_all():
#     response = client.get("/api/users/get-all/", headers={"Authorization": f"Bearer {return_token()}"})

#     assert response.status_code == 200
#     assert len(response.json()) > 0


# # def test_users_get_by_id():

# #     response = client.get("/api/users/get-by-id/1", headers={"Authorization": f"Bearer {return_token()}"})
# #     assert response.status_code == 200
# #     assert len(response.json()) == 1

# # def test_delete_user_by_id():
# #     response = client.delete("/api/users/delete-user-by-id/1", headers={"Authorization": f"Bearer {return_token()}"})
# #     assert response.status_code == 200
# #     assert response.json().get("detail") == "User deleted"


# def test_get_complete_info():
#     response = client.get("/api/users/get-complete-info", headers={"Authorization": f"Bearer {return_token()}"})

#     assert response.status_code == 200
#     pass


# def test_update_my_user():
#     model_body = {
#         "nome": "Test User UPDATE",
#         "email": "user.UPDATE@test.com",
#         "cpf": "38040291593",
#         "pis": "003.57651.58-8",
#         "senha": "senha"
#     }

#     response = client.patch("/api/users/update-my-user", json=model_body, headers={"Authorization": f"Bearer {return_token()}"})
#     assert response.json().get("nome") == "Test User UPDATE"
#     assert response.json().get("email") == "user.UPDATE@test.com"
#     assert response.json().get("cpf") == "38040291593"
#     assert response.json().get("pis") == "00357651588"

#     assert response.status_code == 200
#     pass


# def test_create_address():
#     model_body = {
#         "pais": "EUA",
#         "estado": "SPX",
#         "municipio": "CJAO",
#         "cep": "12460005",
#         "rua": "Agripino Lopes de Moraes",
#         "numero": 500,
#         "complemento": "Hospital",
#         "user_id": 0
#     }

#     response = client.post("/api/address/create", json=model_body, headers={"Authorization": f"Bearer {return_token()}"})

#     assert response.status_code == 201
#     pass


# def test_get_my_address():
#     response = client.get("/api/address/get-my-info", headers={"Authorization": f"Bearer {return_token()}"})

#     assert response.status_code == 200
#     pass


# def test_update_my_address():
#     model_body = {
#         "pais": "BR",
#         "estado": "SP",
#         "municipio": "CJO",
#         "cep": "12460000",
#         "rua": "R. Agripino Lopes de Moraes",
#         "numero": 450,
#         "complemento": "Hospital",
#         "user_id": 0
#     }

#     response = client.patch("/api/address/update-my-address", json=model_body, headers={"Authorization": f"Bearer {return_token()}"})

#     assert response.status_code == 200
#     assert response.json().get("pais") == "BR"
#     assert response.json().get("estado") == "SP"
#     assert response.json().get("municipio") == "CJO"
#     assert response.json().get("cep") == "12460000"
#     assert response.json().get("rua") == "R. Agripino Lopes de Moraes"
#     assert response.json().get("numero") == 450
#     assert response.json().get("complemento") == "Hospital"
#     pass


# def test_get_all_address():
#     response = client.get("/api/address/get-all", headers={"Authorization": f"Bearer {return_token()}"})

#     assert response.status_code == 200
#     assert len(response.json()) > 0
#     pass


# def test_delete_my_address():
#     response = client.delete("/api/address/delete-my-address", headers={"Authorization": f"Bearer {return_token()}"})

#     assert response.status_code == 200
#     pass


# def test_delete_user_my_user():
#     response = client.delete("/api/users/delete-my-user", headers={"Authorization": f"Bearer {return_token()}"})

#     assert response.status_code == 200
#     assert response.json().get("detail") == "User deleted"
#     pass
