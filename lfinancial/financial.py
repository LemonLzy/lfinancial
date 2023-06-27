from lfinancial.factory import GeneratorFactory


class Financial:
    def __init__(self):
        self._generator_factory = GeneratorFactory()

    def _generate(self, generator_name, country):
        generator = self._generator_factory.create_generator(generator_name)
        return generator.gen(generator_name, country)

    def ssn(self, country=None):
        return self._generate("SSN", country)

    def id_card(self, country=None):
        return self._generate("IDCard", country)

    def passport(self, country=None):
        return self._generate("Passport", country)

    def nric(self, country=None):
        return self._generate("NRIC", country)

    def my_number(self, country=None):
        return self._generate("MyNumber", country)

    def first_name(self, country=None):
        return self._generate("first_name", country)

    def middle_name(self, country=None):
        return self._generate("middle_name", country)

    def last_name(self, country=None):
        return self._generate("last_name", country)

    def cn_name(self, country=None):
        return self._generate("cn_name", country)

    def kana_name(self, country=None):
        return self._generate("kana_name", country)


if __name__ == '__main__':
    f = Financial()
    print(f.ssn())
    print(f.id_card())
    print(f.passport())
    print(f.nric())
    print(f.my_number())
    print(f.first_name())
    print(f.middle_name())
    print(f.last_name())
    print(f.kana_name())
    print(f.cn_name())
