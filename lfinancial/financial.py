import random


class Financial:
    def random_id(self):
        prefix = "H"
        random_numbers = str(random.randint(10000000, 99999999))
        return prefix + random_numbers
