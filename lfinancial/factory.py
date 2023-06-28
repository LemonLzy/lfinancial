from lfinancial.generators.document import IDCodeGenerator
from lfinancial.generators.name import NameGenerator
from lfinancial.generators.phone import PhoneGenerator


class GeneratorFactory:
    def __init__(self):
        self.generators = {
            "SSN": IDCodeGenerator(),
            "IDCard": IDCodeGenerator(),
            "Passport": IDCodeGenerator(),
            "NRIC": IDCodeGenerator(),
            "MyNumber": IDCodeGenerator(),
            "first_name": NameGenerator(),
            "middle_name": NameGenerator(),
            "last_name": NameGenerator(),
            "cn_name": NameGenerator(),
            "kana_name": NameGenerator(),
            "cellphone": PhoneGenerator(),
            "area_code": PhoneGenerator(),
        }

    def register_generator(self, name, generator):
        self.generators[name] = generator

    def create_generator(self, name):
        if name in self.generators:
            return self.generators[name]
        raise ValueError(f"Unsupported generator: {name}.")
