from lfinancial.generators.document_type import IDCodeGenerator


class Financial:

    def id_code(self, document_type, country):
        return IDCodeGenerator.generate_id(document_type, country)


if __name__ == '__main__':
    f = Financial()
    print(f.id_code('SSN', 'US'))
    print(f.id_code('SSN', 'US'))
