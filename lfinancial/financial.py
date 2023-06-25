from lfinancial.generators.document_type import IDCodeGenerator


class Financial:

    @staticmethod
    def id_code(document_type, country=None):
        return IDCodeGenerator().generate_id(document_type, country)


if __name__ == '__main__':
    f = Financial()
    print(f.id_code('SSN'))
    print(f.id_code('SSN', 'US'))
