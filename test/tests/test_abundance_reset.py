
import pytest
from elayra.abundance_reset import abundance_reset

def test_abundance_reset_output():
    result = abundance_reset()
    assert isinstance(result, list)
    assert all(symbol in ["E", "C", "P", "S"] for symbol in result)
