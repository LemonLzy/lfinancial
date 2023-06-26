from lfinancial.generators.document_type import IDCodeGenerator


class GeneratorFactory:
    def __init__(self):
        self.generators = {
            'SSN': IDCodeGenerator(),
            'IDCard': IDCodeGenerator(),
            'Passport': IDCodeGenerator(),
            'NRIC': IDCodeGenerator(),
            'MyNumber': IDCodeGenerator(),
        }

    def register_generator(self, name, generator):
        self.generators[name] = generator

    def create_generator(self, name):
        if name in self.generators:
            return self.generators[name]
        raise ValueError(f"Unsupported generator: {name}.")
