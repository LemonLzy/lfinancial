from lfinancial.generators import generate_finance_data


class Financial:
    def random_id(self, country):
        return generate_finance_data(country)
