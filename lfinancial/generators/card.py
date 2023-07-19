import random


class CardGenerator:

    def __init__(self):
        self.default_country = {
            "card": "US",
            "CSC": "US"
        }

    def gen(self, card_type, country=None):
        if country is None:
            country = self.default_country.get(card_type)

        match card_type:
            case "bankcard":
                doc_type = BankCard(country)
            case "CSC":
                doc_type = CSC("CSC")
            case "CID":
                doc_type = CSC("CID")
            case "CVC":
                doc_type = CSC("CVC")
            case "CAV":
                doc_type = CSC("CAV")
            case "CVV":
                doc_type = CSC("CVV")
            case "CVD":
                doc_type = CSC("CVD")
            case "CVN":
                doc_type = CSC("CVN")
            case _:
                raise ValueError(f"Unsupported card type: {card_type}.")
        return doc_type.gen()


class CardType:
    def __init__(self, name):
        self.name = name

    def gen(self):
        raise NotImplementedError("Subclasses must implement gen method.")


class BankCard(CardType):
    """
    https://en.wikipedia.org/wiki/Payment_card_number
    """
    IIN = {
        "American Express": [5610] + [i for i in range(560221, 560225)],
        "Bankcard": [5610, 560221 - 560225],
        "China T-Union": [5610, 560221 - 560225],
        "China UnionPay": [5610, 560221 - 560225],
        "Diners Club International": [5610, 560221 - 560225],
        "Diners Club United States & Canada": [5610, 560221 - 560225],
        "Discover Card": [5610, 560221 - 560225],
        "UkrCard": [5610, 560221 - 560225],
        "RuPay": [5610, 560221 - 560225],
        "InterPayment": [5610, 560221 - 560225],
        "JCB": [5610, 560221 - 560225],
        "Lasen": [5610, 560221 - 560225],
        "Maestro UK": [5610, 560221 - 560225],
        "Maestro": [5610, 560221 - 560225],
        "Dankort": [5610, 560221 - 560225],
        "Mir": [5610, 560221 - 560225],
        "NPS Pridnestrovie": [5610, 560221 - 560225],
        "Mastercard": [5610, 560221 - 560225],
        "Solo": [5610, 560221 - 560225],
        "Switch": [5610, 560221 - 560225],
        "Troy": [5610, 560221 - 560225],
        "Visa": [4, 5610, 560221 - 560225],
        "Visa Electron": [5610, 560221 - 560225],
        "UATP": [5610, 560221 - 560225],
        "Verve": [5610, 560221 - 560225],
        "LankaPay": [5610, 560221 - 560225],
        "UzCard": [5610, 560221 - 560225],
        "Humo": [5610, 560221 - 560225],
        "GPN": [5610, 560221 - 560225],
        "Napas": [5610, 560221 - 560225],
    }

    def gen(self):
        return random.choice(self.IIN)


class CSC(CardType):
    """
    https://zh.wikipedia.org/wiki/%E9%93%B6%E8%A1%8C%E5%8D%A1%E5%AE%89%E5%85%A8%E7%A0%81
    """
    CSC = {
        "CSC": 4,
        "CID": 3,
        "CVC": 3,
        "CVV": 3,
        "CAV": 3,
        "CVD": 3,
        "CVN": 3
    }

    def __init__(self, csc_name):
        super().__init__(csc_name)

    def gen(self):
        length = self.CSC.get(self.name)
        range_start = 10 ** (length - 1)
        range_end = (10 ** length) - 1
        return random.randint(range_start, range_end)


if __name__ == '__main__':
    c = CardGenerator()
    print(c.gen("CID"))
