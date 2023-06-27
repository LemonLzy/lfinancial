from lfinancial.factory import GeneratorFactory


class Financial:
    def __init__(self):
        self._generator_factory = GeneratorFactory()

    def _generate(self, generator_name, country):
        generator = self._generator_factory.create_generator(generator_name)
        return generator.generate_id(generator_name, country)

    def ssn(self, country=None):
        return self._generate('SSN', country)

    def id_card(self, country=None):
        return self._generate('IDCard', country)

    def passport(self, country=None):
        return self._generate('Passport', country)

    def nric(self, country=None):
        return self._generate('NRIC', country)

    def my_number(self, country=None):
        return self._generate('MyNumber', country)


if __name__ == '__main__':
    f = Financial()
    print(f.ssn())
    print(f.id_card())
    print(f.passport())
    print(f.nric())
    print(f.my_number())
