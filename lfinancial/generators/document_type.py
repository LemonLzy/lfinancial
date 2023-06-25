import random


class IDCodeGenerator:

    def __init__(self):
        self.default_country = {
            "SSN": "US",
            "IDCard": "CN",
            # 其他证件类型和默认国家的映射关系
        }

    def generate_id(self, document_type, country=None):
        if country is None:
            country = self.default_country.get(document_type)

        match document_type:
            case "SSN":
                doc_type = SSN()
            case "IDCard":
                doc_type = IDCard()
            case "Passport":
                doc_type = Passport()
            case _:
                raise ValueError(f"Unsupported document type: {document_type}.")

        return doc_type.generate_id(country)


class DocumentType:
    def generate_id(self, country):
        raise NotImplementedError("Subclasses must implement generate_id method.")


class SSN(DocumentType):
    def generate_id(self, country):
        match country:
            case "US":
                return self._generate_us_ssn()
            case _:
                raise ValueError(f"Unsupported country: {country} for SSN generation.")

    @staticmethod
    def _is_valid_ssn(ssn):
        digits = [int(digit) for digit in ssn.replace("-", "")]
        if len(set(digits)) == 1:
            return False

        groups = ssn.split("-")
        for group in groups:
            if int(group) == 0:
                return False

        return True

    def _generate_us_ssn(self):
        # 生成美国 SSN 的具体逻辑
        while True:
            ssn = f"{random.randint(1, 999):03d}-{random.randint(1, 99):02d}-{random.randint(1, 9999):04d}"
            if self._is_valid_ssn(ssn):
                return ssn


class IDCard(DocumentType):
    def generate_id(self, country):
        # 根据国家代码生成身份证号码的逻辑
        # ...
        pass


class Passport(DocumentType):
    def generate_id(self, country):
        # 根据国家代码生成护照号码的逻辑
        # ...
        pass

# 其他证件类型的子类...
