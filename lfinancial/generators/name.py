import random


class NameGenerator:
    def __init__(self):
        self.default_country = {
            "first_name": "US",
            "middle_name": "US",
            "last_name": "US",
            "kana_name": "JP",
            "cn_name": "CN"
        }

    def gen(self, name_type, country=None):
        if country is None:
            country = self.default_country.get(name_type)

        match name_type:
            case "first_name":
                name_type = EnName(country)
            case "last_name":
                name_type = EnName(country)
            case "middle_name":
                name_type = EnName(country)
            case "kana_name":
                name_type = KanaName(country)
            case "cn_name":
                name_type = CNName(country)
            case _:
                raise ValueError(f"Unsupported name type: {name_type}.")

        return name_type.gen()


class NameType:
    def __init__(self, country):
        self.country = country

    def gen(self):
        raise NotImplementedError("Subclasses must implement gen method.")


class EnName(NameType):
    def gen(self):
        match self.country:
            case "US":
                return self._generate_en_name()
            case _:
                raise ValueError(f"Unsupported country: {self.country} for EnName generation.")

    def _generate_en_name(self):
        vowels = "aeiou"
        consonants = "bcdfghjklmnpqrstvwxyz"
        name_length = random.randint(3, 8)
        name = ""

        for i in range(name_length):
            if i % 2 == 0:
                name += random.choice(consonants)
            else:
                name += random.choice(vowels)

        return name.capitalize()


class CNName(NameType):
    def gen(self):
        match self.country:
            case "CN":
                return self._generate_cn_name()
            case _:
                raise ValueError(f"Unsupported country: {self.country} for CNName generation.")

    def _generate_cn_name(self):
        last_name = ["赵", "钱", "孙", "李", "周", "吴", "郑", "王", "冯", "陈", "褚", "卫", "蒋", "沈", "韩", "杨",
                     "朱", "秦", "尤", "许", "何", "吕", "施", "张", "孔", "曹", "严", "华", "金", "魏", "陶", "姜",
                     "戚", "谢", "邹", "喻", "柏", "水", "窦", "章", "云", "苏", "潘", "葛", "奚", "范", "彭", "郎",
                     "鲁", "韦", "昌", "马", "苗", "凤", "花", "方", "任", "袁", "柳", "邓", "史", "薛", "雷", "贺",
                     "倪", "汤", "罗", "毕", "郝", "邬", "安", "常", "乐", "于", "时", "傅", "皮", "卞", "齐", "康",
                     "伍", "余", "元", "卜", "顾", "孟", "平", "黄", "和", "穆", "萧", "尹"]
        first_name_1 = ["子", "仲", "孝", "承", "宏", "家", "可", "立", "美", "楠", "佩", "清", "荣", "诚", "健", "旭",
                        "煜", "泽"]
        first_name_2 = ["芳", "婷", "莉", "玲", "敏", "静", "秀", "娜", "琳", "燕", "洁", "丽", "鑫", "文", "欣", "慧",
                        "雯", "萌", "霞", "蕾", "新", "红", "舒"]

        name = random.choice(last_name)
        name += random.choice(first_name_1)
        if random.random() > 0.5:
            name += random.choice(first_name_2)
        return name


class KanaName(NameType):
    def gen(self):
        match self.country:
            case "JP":
                return self._generate_kana_name()
            case _:
                raise ValueError(f"Unsupported country: {self.country} for KanaName generation.")

    def _generate_kana_name(self):
        katakana = [chr(i) for i in range(0x30a0, 0x30ff + 1)]
        name_length = random.randint(2, 4)
        return "".join([random.choice(katakana) for _ in range(name_length)])
