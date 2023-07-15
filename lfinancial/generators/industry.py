import random


class IndustryGenerator:
    """
    https://en.wikipedia.org/wiki/Global_Industry_Classification_Standard
    """
    industry = (
        "Automobiles & Components",
        "Banks",
        "Capital Goods",
        "Commercial & Professional Services",
        "Consumer Discretionary Distribution & Retail",
        "Consumer Durables & Apparel",
        "Consumer Services",
        "Consumer Staples Distribution & Retail",
        "Energy",
        "Equity Real Estate Investment Trusts (REITs)",
        "Financial Services",
        "Food, Beverage & Tobacco",
        "Health Care Equipment & Services",
        "Household & Personal Products",
        "Insurance",
        "Materials",
        "Media & Entertainment",
        "Pharmaceuticals, Biotechnology & Life Sciences",
        "Real Estate Management & Development",
        "Semiconductors & Semiconductor Equipment",
        "Software & Services",
        "Technology Hardware & Equipment",
        "Telecommunication Services",
        "Transportation",
        "Utilities",
    )

    def gen(self, *args, **kwargs):
        return random.choice(self.industry)


if __name__ == "__main__":
    i = IndustryGenerator()
    print(i.gen())
