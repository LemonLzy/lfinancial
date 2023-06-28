from unittest import TestCase

from lfinancial import Financial
from lfinancial.generators.document import SSN

financial = Financial()


class TestSSN(TestCase):

    def test_generate_id(self):
        ssn = financial.ssn()
        assert len(ssn) == 11
        assert SSN._is_valid_ssn(ssn)
