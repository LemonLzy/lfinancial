import random
import re
import string


class IDCodeGenerator:

    def __init__(self):
        self.default_country = {
            "SSN": "US",
            "IDCard": "CN",
            "Passport": "CN"
            # 其他证件类型和默认国家的映射关系
        }

    def generate_id(self, document_type, country=None):
        if country is None:
            country = self.default_country.get(document_type)

        match document_type:
            case "SSN":
                doc_type = SSN(country)
            case "IDCard":
                doc_type = IDCard(country)
            case "Passport":
                doc_type = Passport(country)
            case _:
                raise ValueError(f"Unsupported document type: {document_type}.")

        return doc_type.generate_id()


class DocumentType:
    def __init__(self, country):
        self.country = country

    def generate_id(self):
        raise NotImplementedError("Subclasses must implement generate_id method.")

    def check_code(self, id_code: str):
        raise NotImplementedError("Subclasses must implement check_code method.")


class SSN(DocumentType):
    def generate_id(self):
        match self.country:
            case "US":
                return self._generate_us_ssn()
            case _:
                raise ValueError(f"Unsupported country: {self.country} for SSN generation.")

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
    def generate_id(self):
        match self.country:
            case "CN":
                return self._generate_cn_id()
            case _:
                raise ValueError(f"Unsupported country: {self.country} for IDCard generation.")

    def _generate_cn_id(self):
        # 随机生成一个区域码(6位数)
        region_code = str(random.randint(110000, 659004))
        # 生成年份(4位数)
        year = str(random.randint(1949, 2022))
        # 生成月份(2位数)
        month = str(random.randint(1, 12)).rjust(2, '0')
        # 生成日期(2位数)
        day = str(random.randint(1, 28)).rjust(2, '0')
        # 生成顺序码(3位数)
        order = str(random.randint(1, 999)).rjust(3, '0')
        # 生成校验码(1位数)
        check_code = self.check_code(region_code + year + month + day + order)
        # 拼接身份证号码并返回
        return region_code + year + month + day + order + check_code

    def check_code(self, id_code):
        # 系数列表
        factor_list = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
        # 校验码列表
        check_code_list = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
        # 根据前17位计算出校验码
        check_code = 0
        for i in range(len(id_code)):
            check_code += int(id_code[i]) * factor_list[i]
        check_code %= 11
        return check_code_list[check_code]


class Passport(DocumentType):
    def generate_id(self):
        match self.country:
            case "CN":
                return self._generate_cn_passport()
            case _:
                raise ValueError(f"Unsupported country: {self.country} for IDCard generation.")

    def _generate_cn_passport(self):
        """
        中国普通护照 (电子护照)E开头+8位数字 或 E+字母+7位数字 (E12345678/ED1234567)
        """
        first = "E"
        second = random.choice(string.ascii_uppercase + string.digits)
        other = random.randint(0000000, 9999999)

        return f"{first}{second}{other}"
