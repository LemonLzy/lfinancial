import random


class StockGenerator:

    def __init__(self):
        self.default_country = {
            "stock_exchange": "US",
            "ticker_symbol": "US",
            "product": "US"
        }

    def gen(self, stock_type, country):
        if country is None:
            country = self.default_country.get(stock_type)

        match stock_type:
            case "stock_exchange":
                stock_type = StockExchange(country)
            case "ticker_symbol":
                stock_type = TickerSymbol(country)
            case "product":
                stock_type = TradeProduct(country)
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


class TickerSymbol(StockType):
    ticker_symbols = (
        "AAPL",
        "ABT",
        "ACLS",
        "ACM",
        "ACN",
        "ADBE",
        "AKAM",
        "AMD",
        "AMGN",
        "AMZN",
        "ATHM",
        "ATI",
        "BABA",
        "BAX",
        "BIDU",
        "BILI",
        "BMY",
        "CMCM",
        "CPB",
        "CRM",
        "CSCO",
        "CTRP",
        "CTSH",
        "CVS",
        "DCM",
        "DELL",
        "DOYU",
        "EBAY",
        "EDU",
        "EQIX",
        "ERIC",
        "FUTU",
        "GLW",
        "GOOG",
        "GRPN",
        "HPQ",
        "IBM",
        "INFA",
        "INTC",
        "JBL",
        "JD",
        "JNJ",
        "JNPR",
        "KLAC",
        "KO",
        "MCD",
        "MCHP",
        "MDT",
        "MO",
        "MRK",
        "MSFT",
        "MSI",
        "NFLX",
        "NOK",
        "NOW",
        "NTAP",
        "NTES",
        "NVDA",
        "ORCL",
        "PDD",
        "PEP",
        "PFE",
        "QCOM",
        "QFIN",
        "QTT",
        "S",
        "SAP",
        "SBUX",
        "SE",
        "SMAR",
        "STX",
        "SYMC",
        "T",
        "TCEHY",
        "TDS",
        "TER",
        "TRIP",
        "TXN",
        "TYL",
        "UNH",
        "VIPS",
        "VMW",
        "VOD",
        "VRSN",
        "VZ",
        "WUBA",
        "YELP",
        "YNDX",
        "YUMC",
        "YY",
    )

    def gen(self):
        return random.choice(self.ticker_symbols)


class TradeProduct(StockType):
    product = (
        "A-shares",
        "ADR",
        "Bond",
        "Business Trusts",
        "Callable Bull/Bear Contract",
        "Closed-end Funds",
        "Crypto",
        "DLCs",
        "ETFs",
        "Foreign Exchange Futures",
        "Fractional Shares",
        "Futures",
        "Index",
        "Inside Certificate",
        "Leveraged Foreign Exchange",
        "Preference Shares",
        "REITs",
        "Share Price Index Futures",
        "Shares",
        "Stock Index Option",
        "Stock Option",
        "Trusts",
        "Warrants"
    )

    def gen(self):
        return random.choice(self.product)
