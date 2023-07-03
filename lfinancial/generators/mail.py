import random


class EmailGenerator:
    def __init__(self):
        self.default_suffix = "gmail"

    def gen(self, mail_type, suffix=None):
        letters = 'abcdefghijklmnopqrstuvwxyz'
        digits = '0123456789'
        prefix = ['hotmail', 'gmail', 'yahoo', 'outlook', 'icloud'] if suffix is None else [self.default_suffix]
        tlds = ['com', 'org', 'net', 'edu']

        name_length = random.randint(10, 20)
        name = ''.join(random.choices(letters + digits, k=name_length))

        domain_prefix = random.choice(prefix)
        tld = random.choice(tlds)

        email = f'{name}@{domain_prefix}.{tld}'
        return email


if __name__ == '__main__':
    print(EmailGenerator().gen())
