import random


class CountryGenerator:
    def gen(self, country_type, country=None):
        match country_type:
            case "high_risk":
                country = HighRiskCountry(country)
            case _:
                raise ValueError(f"Unsupported document type: {country_type}.")

        return country.gen()


class CountryType:
    def __init__(self, country):
        self.country = country

    def gen(self):
        raise NotImplementedError("Subclasses must implement gen method.")


class HighRiskCountry(CountryType):
    _high = [
        "AL",
        "BR",
        "ET",
        "AO",
        "AL",
        "DZ",
        "AF",
        "AE",
        "BY",
        "BB",
        "PK",
        "PY",
        "PS",
        "PA",
        "MP",
        "BW",
        "PR",
        "BF",
        "GQ",
        "TG",
        "ER",
        "RU",
        "PH",
        "CG",
        "GE",
        "GU",
        "GY",
        "CU",
        "TH",
        "NH",
        "KH",
        "GH",
        "ZW",
        "DJ",
        "KG",
        "GN",
        "KY",
        "KE",
        "LB",
        "LR",
        "LY",
        "RW",
        "MU",
        "MG",
        "MV",
        "TM",
        "ML",
        "UM",
        "AS",
        "VI",
        "MN",
        "MM",
        "MD",
        "MA",
    ]

    def gen(self):
        return random.choice(self._high)


if __name__ == '__main__':
    risk = HighRiskCountry("").gen()
    print(risk)
    print(type(risk))
