from lfinancial.factory import GeneratorFactory


class Financial:
    def __init__(self):
        self._generator_factory = GeneratorFactory()

    def __generate(self, generator_name, country):
        generator = self._generator_factory.create_generator(generator_name)
        return generator.gen(generator_name, country)

    def ssn(self, country=None):
        return self.__generate("SSN", country)

    def id_card(self, country=None):
        return self.__generate("IDCard", country)

    def passport(self, country=None):
        return self.__generate("Passport", country)

    def nric(self, country=None):
        return self.__generate("NRIC", country)

    def my_number(self, country=None):
        return self.__generate("MyNumber", country)

    def first_name(self, country=None):
        return self.__generate("first_name", country)

    def middle_name(self, country=None):
        return self.__generate("middle_name", country)

    def last_name(self, country=None):
        return self.__generate("last_name", country)

    def cn_name(self, country=None):
        return self.__generate("cn_name", country)

    def kana_name(self, country=None):
        return self.__generate("kana_name", country)

    def cellphone(self, country=None):
        return self.__generate("cellphone", country)

    def area_code(self, country=None):
        return self.__generate("area_code", country)

    def high_risk_country(self, country=None):
        return self.__generate("high_risk", country)

    def email(self, suffix=None):
        return self.__generate("email", suffix)

    def bank(self, country=None):
        return self.__generate("bank", country)


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
    print(f.cellphone())
    print(f.area_code())
    print(f.high_risk_country())
    print(f.email())
    print(f.bank())
