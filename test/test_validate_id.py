import pytest
from tube.validate_id import valid_id

def test_valid_id_true():
    assert(valid_id('7a5EWYpRFAY') == True)

