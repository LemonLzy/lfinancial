import random


class DocumentType:
    def generate_id(self, country):
        raise NotImplementedError("Subclasses must implement generate_id method.")


class SSN(DocumentType):
    def generate_id(self, country):
        # 根据国家代码生成 SSN 的逻辑
        if country == 'US':
            # 生成美国的 SSN
            return self._generate_us_ssn()
        elif country == 'SG':
            # 生成新加坡的 SSN
            return self._generate_sg_ssn()
        else:
            raise ValueError(f"Unsupported country: {country} for SSN generation.")

    def _generate_us_ssn(self):
        # 生成美国 SSN 的具体逻辑
        # ...
        pass

    def _generate_sg_ssn(self):
        # 生成新加坡 SSN 的具体逻辑
        # ...
        pass


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

class IDCodeGenerator:

    @staticmethod
    def generate_id(document_type, country):
        if document_type == 'SSN':
            doc_type = SSN()
        elif document_type == 'IDCard':
            doc_type = IDCard()
        elif document_type == 'Passport':
            doc_type = Passport()
        else:
            raise ValueError(f"Unsupported document type: {document_type}.")

        return doc_type.generate_id(country)
