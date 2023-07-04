import random


class BankGenerator:
    bank_names = (
        'AFB Bank',
        'AccessBank',
        'Agricultural Bank of China Limited',
        'Argentaria SA',
        'BANK OF CHINA (HONG KONG) LIMITED',
        'BNP Paribas',
        'BPCE',
        'Banco Bilbao Vizcaya',
        'Banco Santander, S.A.',
        'Bank BTB',
        'Bank Melli Iran',
        'Bank of America National Association',
        'Bank of China Limited',
        'Bank of Communications Co Ltd',
        'Bank of Montreal',
        'Banque Fédérative du Crédit Mutue',
        'Barclays Bank PLC',
        'CaixaBank SA',
        'China Citic Bank Corporation Limited',
        'China Construction Bank Corporation',
        'China Development Bank',
        'China Everbright Bank Co Ltd',
        'China Merchants Bank Co Ltd',
        'China Minsheng Banking Corporation Limited',
        'Citibank (Hong Kong) Limited',
        'Citibank, N.A.',
        'Commonwealth Bank of Australia',
        'Credit Suisse AG',
        'DBS Bank',
        'Deutsche Bank AG',
        'First Republic Bank',
        'HSBC Bank plc',
        'ING Bank NV',
        'Industrial and Commercial Bank of China Limited',
        'Intesa Sanpaolo SPA',
        'JAPAN POST BANK Co Ltd',
        'JPMorgan Chase Bank National Association',
        'La Banque Postale',
        'Lloyds Bank Plc',
        'MUFG Bank Ltd.',
        'Mitsubishi UFJ Financial Group, Inc.',
        'Mizuho Bank Ltd',
        'National Bank of Pakistan',
        'Ping An Bank Co Ltd',
        'Postal Savings Bank of China Co Ltd',
        'Premium Bank',
        'Royal Bank of Canada',
        'Shanghai Pudong Development Bank',
        'Signature Bank',
        'Silicon Valley Bank',
        'Société Générale',
        'Standard Chartered Bank',
        'Sumitomo Mitsui Banking Corporation',
        'The Agricultural Development Bank of China',
        'The Bank of Nova Scotia',
        'The Export-Import Bank of China',
        'The Hongkong and Shanghai Banking Corporation Limited',
        'The Norinchukin Bank',
        'The Toronto-Dominion Bank',
        'U.S. Bancorp',
        'UBS AG',
        'UniCredit SpA',
        'Wells Fargo Bank National Association',
        'ZA Bank'
    )

    def gen(self, *args, **kwargs):
        """Generate a bank name."""
        return random.choice(self.bank_names)


if __name__ == '__main__':
    print(BankGenerator().gen())
