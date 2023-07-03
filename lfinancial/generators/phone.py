import random
from enum import Enum

from lfinancial.generators.const import Country


class PhoneCode(Enum):
    CN = "+86"  # 中国
    US = "+1"  # 美国
    JP = "+81"  # 日本
    IN = "+91"  # 印度
    GB = "+44"  # 英国
    DE = "+49"  # 德国
    FR = "+33"  # 法国
    KR = "+82"  # 韩国
    AU = "+61"  # 澳大利亚
    CA = "+1"  # 加拿大
    MX = "+52"  # 墨西哥
    BR = "+55"  # 巴西
    IT = "+39"  # 意大利
    ES = "+34"  # 西班牙
    RU = "+7"  # 俄罗斯
    SA = "+966"  # 沙特阿拉伯
    AE = "+971"  # 阿联酋


class PhoneGenerator:
    def __init__(self):
        self.default_country = {
            "cellphone": "CN",
            "area_code": "CN",
            "telephone": "CN",
            "cornet": "CN",
        }

    def gen(self, phone_type, country=None):
        if country is None:
            country = self.default_country.get(phone_type)

        match phone_type:
            case "cellphone":
                phone_type = CellPhone(country)
            case "area_code":
                phone_type = AreaCode(country)
            case _:
                raise ValueError(f"Unsupported phone type: {phone_type}.")

        return phone_type.gen()


class PhoneType:
    def __init__(self, country):
        self.country = country

    def gen(self):
        raise NotImplementedError("Subclasses must implement gen method.")


class CellPhone(PhoneType):
    def gen(self):
        match self.country:
            case "CN":
                return self._generate_cn_cellphone()
            case "US":
                return self._generate_us_cellphone()
            case _:
                raise ValueError(f"Unsupported country: {self.country} for cellphone generation.")

    def _generate_cn_cellphone(self):
        # 号码段，前三位为移动号段
        mobile_segments = [
            "134", "135", "136", "137", "138", "139", "147", "150", "151", "152",
            "157", "158", "159", "165", "172", "178", "182", "183", "184", "187",
            "188", "195", "197", "198", "199"
        ]

        # 随机选择一个号码段
        mobile_segment = random.choice(mobile_segments)

        province_code = str(random.randint(10, 99))
        user_number = str(random.randint(100000, 999999))

        mobile_number = mobile_segment + province_code + user_number

        return mobile_number

    def _generate_us_cellphone(self):
        mobile_segments = [
            "201", "202", "203", "204", "205", "206", "207", "208", "209", "210",
            "212", "213", "214", "215", "216", "217", "218", "219", "224", "225",
            "228", "229", "231", "234", "236", "239", "240", "248", "251", "252",
            "253", "254", "256", "260", "262", "267", "269", "270", "272", "276",
            "281", "283", "301", "302", "303", "304", "305", "307", "308", "309",
            "310", "312", "313", "314", "315", "316", "317", "318", "319", "320",
            "321", "323", "325", "327", "330", "331", "334", "336", "337", "339",
            "340", "341", "343", "345", "346", "347", "351", "352", "360", "361",
            "364", "380", "385", "386", "401", "402", "404", "405", "406", "407",
            "408", "409", "410", "412", "413", "414", "415", "417", "419", "423",
            "424", "425", "430", "432", "434", "435", "440", "442", "443", "447",
            "458", "463", "469", "470", "475", "478", "479", "480", "484", "501",
            "502", "503", "504", "505", "507", "508", "509", "510", "512", "513",
            "515", "516", "517", "518", "520", "530", "531", "534", "539", "540",
            "541", "551", "559", "561", "562", "563", "564", "567", "570", "571",
            "573", "574", "575", "580", "585", "586", "601", "602", "603", "605",
            "606", "607", "608", "609", "610", "612", "614", "615", "616", "617",
            "618", "619", "620", "623", "626", "628", "629", "630", "631", "636",
            "641", "646", "650", "651", "657", "660", "661", "662", "667", "669",
            "678", "680", "681", "682", "684", "701", "702", "703", "704", "706",
            "707", "708", "712", "713", "714", "715", "716", "717", "718", "719",
            "720", "724", "725", "726", "727", "731", "732", "734", "737", "740",
            "747", "752", "754", "757", "760", "762", "763", "765", "769", "770",
            "772", "773", "774", "775", "779", "781", "785", "786", "801", "802",
            "803", "804", "805", "806", "808", "810", "812", "813", "814", "815",
            "816", "817", "818", "828", "830", "831", "832", "838", "843", "845",
            "847", "848", "850", "854", "856", "857", "858", "859", "860", "862",
            "863", "864", "865", "870", "872", "878", "901", "903", "904", "906",
            "907", "908", "909", "910", "912", "913", "914", "915", "916", "917",
            "918", "919", "920", "925", "928", "929", "930", "931", "934", "936",
            "937", "938", "939", "940", "941", "947", "949", "951", "952", "954",
            "956", "959", "970", "971", "972", "973", "978", "979", "980", "984",
            "985", "989"
        ]

        # 随机选择一个号码段
        mobile_segment = random.choice(mobile_segments)

        # 随机生成用户号码，后四位为用户号码
        user_number = str(random.randint(1000, 9999))

        # 拼接号码段和用户号码
        mobile_number = mobile_segment + user_number

        return mobile_number


class AreaCode(PhoneType):
    def gen(self):
        country_code = self.country
        if isinstance(country_code, Country):
            country_code = country_code.value

        if isinstance(country_code, str):
            try:
                return PhoneCode[country_code].value
            except KeyError:
                return None

        return None
