from passlib.context import CryptContext
import re

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash(password: str):
    return pwd_context.hash(password)


def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


# https://stackoverflow.com/questions/20558699/python-how-recursively-remove-none-values-from-a-nested-data-structure-lists-a
def remove_none(obj):
    if isinstance(obj, (list, tuple, set)):
        return type(obj)(remove_none(x) for x in obj if x is not None)
    elif isinstance(obj, dict):
        return type(obj)((remove_none(k), remove_none(v))
                         for k, v in obj.items() if k is not None and v is not None)
    else:
        return obj


class Validator:
    @staticmethod
    def validateCPF(cpf):
        cpf = re.sub('\D', '', cpf.replace('.', '').replace('-', ''))

        if not cpf:
            return False

        if len(cpf) != 11:
            return False

        if cpf == (cpf[0] * len(cpf)):
            return False

        # Variables
        sum_values_1 = 0
        digit_one = 0

        sum_values_2 = 0
        digit_two = 0

        # CALC FOR FIRST DIGIT
        for key, multiply in enumerate(range(len(cpf)-1, 1, -1)):
            sum_values_1 += int(cpf[key]) * multiply

        digit_one = 11 - (sum_values_1 % 11)
        digit_one = digit_one if digit_one <= 9 else 0

        # CALC FOR SECOND DIGIT
        for key, multiply in enumerate(range(len(cpf), 1, -1)):
            sum_values_2 += int(cpf[key]) * multiply

        digit_two = (sum_values_2 * 10) % 11

        if digit_one != int(cpf[9]) or digit_two != int(cpf[10]):
            return False

        return True

    @staticmethod
    def validatePIS(pis):
        pis = re.sub('\D', '', pis.replace('.', '').replace('-', ''))

        if not pis:
            return False

        if len(pis) != 11:
            return False

        if pis == (pis[0] * len(pis)):
            return False

        # Variables
        sum_values_1 = 0
        digit_one = 0

        # CALC FOR FIRST DIGIT
        pis_weight = [3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        for key, multiply in enumerate(pis_weight):
            sum_values_1 += int(pis[key]) * multiply

        digit_one = 11 - (sum_values_1 % 11)
        digit_one = digit_one if digit_one <= 9 else 0

        if digit_one != int(pis[10]):
            return False

        return True


if __name__ == '__main__':
    print('PIS: ' + str(Validator.validatePIS('722.5189305-4')))  # TRUE
    print('CPF: ' + str(Validator.validateCPF('490.027.928-59')))  # TRUE

    print('PIS: ' + str(Validator.validatePIS('722.5189305-9')))  # FALSE
    print('CPF: ' + str(Validator.validateCPF('490.027.928-58')))  # FALSE
