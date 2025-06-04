
import pytest
from elayra.semantic_crispr import crispr_insert, entropy_check, entropy_based_primer

def test_crispr_insert():
    result = crispr_insert(["E", "P"], "S", 1)
    assert result == ["E", "S", "P"]

def test_entropy_check():
    entropy = entropy_check(["E", "E", "P", "S"])
    assert 0 <= entropy <= 1

def test_entropy_based_primer():
    primer = entropy_based_primer(["E", "P"])
    assert len(primer) == 4
