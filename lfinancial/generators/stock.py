import random


class StockGenerator:

    def __init__(self):
        self.default_country = {
            "stock_exchange": "US"
        }

    def gen(self, stock_type, country):
        if country is None:
            country = self.default_country.get(stock_type)

        match stock_type:
            case "stock_exchange":
                stock_type = StockExchange(country)
            # case "ticker_symbol":
            #     stock_type = TickerSymbol(country)
            case _:
                raise ValueError(f"Unsupported name type: {stock_type}.")

        return stock_type.gen()


class StockType:
    def __init__(self, country):
        self.country = country

    def gen(self):
        raise NotImplementedError("Subclasses must implement gen method.")


class StockExchange(StockType):

    """
    https://en.wikipedia.org/wiki/List_of_stock_exchanges
    """
    stock_exchanges = (
        "Australian Securities Exchange",
        "B3 Brasil Bolsa Balcão,",
        "Bombay Stock Exchange",
        "Deutsche Börse AG",
        "Euronext",
        "Hong Kong Stock Exchange",
        "Japan Exchange Group",
        "Johannesburg Stock Exchange",
        "Korea Exchange",
        "London Stock Exchange",
        "Nasdaq",
        "Nasdaq Nordic and Baltic Exchanges",
        "National Stock Exchange",
        "New York Stock Exchange",
        "SIX Swiss Exchange",
        "Saudi Stock Exchange (Tadawul)",
        "Shanghai Stock Exchange",
        "Shenzhen Stock Exchange",
        "Taiwan Stock Exchange",
        "Tehran Stock Exchange",
        "Toronto Stock Exchange"
    )

    def gen(self):
        return random.choice(self.stock_exchanges)
