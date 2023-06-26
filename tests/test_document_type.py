from unittest import TestCase

from lfinancial import Financial
from lfinancial.generators.document_type import SSN

financial = Financial()


class TestSSN(TestCase):

    def test_generate_id(self):
        ssn = financial.id_code("SSN")
        assert len(ssn) == 11
        assert SSN._is_valid_ssn(ssn)
