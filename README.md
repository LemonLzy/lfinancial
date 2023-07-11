lfinancial is a Python package that generates financial fake data.

---
```
.-.    .----. .-. .-. .-.   .--.   .-. .-. .----. .-.   .--.   .-.    
} |    } |__} { | |  \{ |  / {} \  |  \{ | | }`-' { |  / {} \  } |    
} '--. } '_}  | } | }\  { /  /\  \ | }\  { | },-. | } /  /\  \ } '--. 
`----' `--'   `-' `-' `-' `-'  `-' `-' `-' `----' `-' `-'  `-' `----' 
```
[![pypi](https://img.shields.io/pypi/v/lfinancial)](https://pypi.org/project/lfinancial/)
[![GitHub Workflow Status (with event)](https://img.shields.io/github/actions/workflow/status/LemonLzy/lfinancial/publish.yml)](https://github.com/LemonLzy/lfinancial/actions)
[![GitHub](https://img.shields.io/github/license/LemonLzy/lfinancial)](https://github.com/LemonLzy/lfinancial/blob/main/LICENSE.txt)
---

#### How to install?
```shell
pip install lfinancial
```

#### How to use it? 
```python
from lfinancial import Financial

f = Financial()

f.ssn()
# 582-94-2808

f.id_card()
# 488258196409087762

f.passport()
# EG4130431

f.nric()
# SD44949622

f.my_number()
# 399495927695

f.cn_name()
# 于诚玲

f.first_name()
# Cakadiq

f.middle_name()
# Baviv

f.last_name()
# Hucacuqa

f.kana_name()
# ハジ

f.cellphone()
# 13851695115

f.area_code()
# +86

f.high_risk_country()
# MA

f.email()
# q0o58mkgq3@gmail.com

f.bank()
# BANK OF CHINA (HONG KONG) LIMITED

f.currency()
# CNY

f.swift_code()
# ABOCCNBJ040

f.stock_exchange()
# Hong Kong Stock Exchange

f.ticker_symbol()
# AAPL

f.tz_identifier()
# Asia/Baku

f.locale()
# zh-CN

f.product()
# Shares
```