from app.utils.utils import Validator


def test_validate_cpf():
  # TEST TRUE
    assert Validator.validateCPF(cpf='072.618.340-76') == True
    assert Validator.validateCPF(cpf='07261834076') == True
    assert Validator.validateCPF(cpf='072 . 618 -340.76') == True
    assert Validator.validateCPF(cpf='0 7 2 6 1 8 3 4 0 7 6') == True
    assert Validator.validateCPF(cpf='0-7-2-6-1-8-3-4-0-7-6') == True
    assert Validator.validateCPF(cpf='0.7.2.6.1.8.3.4.0.7.6') == True
  # TEST FALSE
    assert Validator.validateCPF(cpf='072.618.340-75') == False
    assert Validator.validateCPF(cpf='07261834075') == False
    assert Validator.validateCPF(cpf='072 . 618 -340.75') == False
    assert Validator.validateCPF(cpf='0 7 2 6 1 8 3 4 0 7 5') == False
    assert Validator.validateCPF(cpf='0-7-2-6-1-8-3-4-0-7-5') == False
    assert Validator.validateCPF(cpf='0.7.2.6.1.8.3.4.0.7.5') == False


def test_validate_pis():
    # TEST TRUE
    assert Validator.validatePIS(pis='896.61823.68-9') == True
    assert Validator.validatePIS(pis='89661823689') == True
    assert Validator.validatePIS(pis='8 96 . 618 23 .6 8 -9') == True
    assert Validator.validatePIS(pis='8 9 6 6 1 8 2 3 6 8 9') == True
    assert Validator.validatePIS(pis='8-9-6-6-1-8-2-3-6-8-9') == True
    assert Validator.validatePIS(pis='8.9.6.6.1.8.2.3.6.8.9') == True
  # TEST FALSE
    assert Validator.validatePIS(pis='896.61823.68-1') == False
    assert Validator.validatePIS(pis='89661823681') == False
    assert Validator.validatePIS(pis='8 96 . 618 23 .6 8 -1') == False
    assert Validator.validatePIS(pis='8 9 6 6 1 8 2 3 6 8 1') == False
    assert Validator.validatePIS(pis='8-9-6-6-1-8-2-3-6-8-1') == False
    assert Validator.validatePIS(pis='8.9.6.6.1.8.2.3.6.8.1') == False


def test_validate_email():
  # TEST TRUE
    assert Validator.validateEMAIL('example.1@example.com') == True
    assert Validator.validateEMAIL('example.1@example.br') == True
    assert Validator.validateEMAIL('example@email.com') == True
  # TEST FALSE
    assert Validator.validateEMAIL('example.1@example') == False
    assert Validator.validateEMAIL('example.1@example@email.com') == False
    assert Validator.validateEMAIL('example.1@.com') == False
    assert Validator.validateEMAIL('example.1@example.com.br') == False
    assert Validator.validateEMAIL('example.1@example-home.com') == False
    assert Validator.validateEMAIL('example.1example.com') == False
