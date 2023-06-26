LFinancial is a Python package that generates financial fake data.

#### How to install?
```shell
pip install lfinancial
```

#### How to use it? 
```python
from lfinancial import Financial


f = Financial()

f.id_code('SSN')
f.id_code('SSN', 'US')
f.id_code('IDCard', 'CN')
f.id_code('Passport')
f.id_code('NRIC')
f.id_code('MyNumber')
```