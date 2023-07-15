class CardGenerator:
    """
    https://en.wikipedia.org/wiki/Payment_card_number
    """
    IIN = {
        "American Express": [5610, [i for i in range(560221, 560225)]],
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


if __name__ == '__main__':
    c = CardGenerator()
    print(c.IIN)
