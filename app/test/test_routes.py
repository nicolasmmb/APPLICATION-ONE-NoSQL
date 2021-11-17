from fastapi import FastAPI
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    pass


def return_token() -> str:
    model_body = {
        "cpf": "38040291593",
        "senha": "senha"
    }

    response = client.post("/auth/login", json=model_body)
    token_auth = response.json().get("token")

    return token_auth


def test_create_user():
    model_body = {
        "nome": "Test User",
        "email": "user@test.com",
        "cpf": "38040291593",
        "pis": "003.57651.58-8",
        "senha": "senha",
        "endereco": {
            "pais": "BRX",
            "estado": "SPX",
            "municipio": "CJOX",
            "cep": "12460000",
            "rua": "Agripino Lopes de Moraes",
            "numero": 500,
            "complemento": "Hospital"
        }
    }

    response = client.post("/api/users/create", json=model_body)
    assert response.status_code == 201
    pass


def test_get_token():
    model_body = {
        "cpf": "38040291593",
        "senha": "senha"
    }

    response = client.post("/auth/login", json=model_body)
    token_auth = response.json().get("token")

    assert response.status_code == 200
    pass


def test_users_get_all():
    response = client.get("/api/users/get-all/", headers={"Authorization": f"Bearer {return_token()}"})

    assert response.status_code == 200
    assert len(response.json().get("response")) > 0
    pass


def test_update_my_user():
    model_body = {
        "nome": "Test User Update",
        "email": "user.UPDATE@test.com",
        "cpf": "38040291593",
        "pis": "003.57651.58-8",
        "senha": "senha",
        "endereco": {
            "pais": "BR",
            "estado": "SP",
            "municipio": "CJO",
            "cep": "12460000",
            "rua": "R. Agripino Lopes de Moraes",
            "numero": 450,
            "complemento": "Hospital"
        }
    }

    response = client.put("/api/users/update-my-user", json=model_body, headers={"Authorization": f"Bearer {return_token()}"})
    reposonse_body = response.json()["response"]
    assert response.status_code == 200
    assert reposonse_body["nome"] == "Test User Update"
    assert reposonse_body["email"] == "user.UPDATE@test.com"
    assert reposonse_body["cpf"] == "38040291593"
    assert reposonse_body["pis"] == "00357651588"
    assert reposonse_body["endereco"]["pais"] == "BR"
    assert reposonse_body["endereco"]["estado"] == "SP"
    assert reposonse_body["endereco"]["municipio"] == "CJO"
    assert reposonse_body["endereco"]["cep"] == "12460000"
    assert reposonse_body["endereco"]["rua"] == "R. Agripino Lopes de Moraes"
    assert reposonse_body["endereco"]["numero"] == 450
    assert reposonse_body["endereco"]["complemento"] == "Hospital"
    pass


def test_delete_my_user():
    response = client.delete("/api/users/delete-my-user", headers={"Authorization": f"Bearer {return_token()}"})
    assert response.status_code == 200
    assert response.json().get("message") == "User Deleted"
    pass
