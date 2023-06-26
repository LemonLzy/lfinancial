from lfinancial.generators.document_type import IDCodeGenerator


class Financial:

    @staticmethod
    def id_code(document_type, country=None):
        return IDCodeGenerator().generate_id(document_type, country)


if __name__ == '__main__':
    f = Financial()
    print(f.id_code('SSN'))
    print(f.id_code('SSN', 'US'))
    print(f.id_code('IDCard'))
    print(f.id_code('IDCard', 'CN'))
    print(f.id_code('Passport'))
    print(f.id_code('Passport', 'CN'))
    print(f.id_code('NRIC'))
    print(f.id_code('NRIC', 'SG'))
    print(f.id_code('MyNumber'))
    print(f.id_code('MyNumber', 'JP'))
