import random


def generate_hk_id():
    prefix = "H"
    random_numbers = str(random.randint(10000000, 99999999))
    return prefix + random_numbers


def generate_sg_id():
    prefix = "S"
    random_numbers = str(random.randint(10000000, 99999999))
    return prefix + random_numbers


def generate_passport_number():
    prefix = "P"
    random_numbers = str(random.randint(10000000, 99999999))
    return prefix + random_numbers


def generate_finance_data(country):
    match country:
        case "HK":
            return generate_hk_id()
        case "SG":
            return generate_sg_id()
        case "Passport":
            return generate_passport_number()
        case _:
            raise ValueError("Unsupported country")
