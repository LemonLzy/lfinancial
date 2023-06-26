LFinancial is a Python package that generates financial fake data.

---
```
.-.    .----. .-. .-. .-.   .--.   .-. .-. .----. .-.   .--.   .-.    
} |    } |__} { | |  \{ |  / {} \  |  \{ | | }`-' { |  / {} \  } |    
} '--. } '_}  | } | }\  { /  /\  \ | }\  { | },-. | } /  /\  \ } '--. 
`----' `--'   `-' `-' `-' `-'  `-' `-' `-' `----' `-' `-'  `-' `----' 
```
[![pypi](https://img.shields.io/pypi/v/lfinancial)](https://pypi.org/project/lfinancial/)
![GitHub Workflow Status (with event)](https://img.shields.io/github/actions/workflow/status/LemonLzy/lfinancial/publish.yml)
![GitHub](https://img.shields.io/github/license/LemonLzy/lfinancial)
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
```