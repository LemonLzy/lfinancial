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

    def cellphone(self, country=None):
        return self._generate("cellphone", country)

    def area_code(self, country=None):
        return self._generate("area_code", country)

    def high_risk_country(self, country=None):
        return self._generate("high_risk", country)

    def email(self, suffix=None):
        return self._generate("email", suffix)

    def bank(self, country=None):
        return self._generate("bank", country)

    def currency(self, country=None):
        return self._generate("currency", country)

    def swift_code(self, country=None):
        return self._generate("swift_code", country)

    def stock_exchange(self, country=None):
        return self._generate("stock_exchange", country)

    def ticker_symbol(self, country=None):
        return self._generate("ticker_symbol", country)

    def tz_identifier(self, country=None):
        return self._generate("tz_identifier", country)

    def locale(self, country=None):
        return self._generate("locale", country)

    def product(self, country=None):
        return self._generate("product", country)


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
    print(f.currency())
    print(f.swift_code())
    print(f.stock_exchange())
    print(f.ticker_symbol())
    print(f.tz_identifier())
    print(f.locale())
    print(f.product())
