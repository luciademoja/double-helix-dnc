from elayra.semantic_crispr import crispr_insert, entropy_check, entropy_based_primer

def test_crispr_insert():
    result = crispr_insert(["E", "S", "P"], "C", 1)
    assert result == ["E", "C", "S", "P"]

def test_entropy_check():
    filament = ["E", "E", "E", "E"]
    assert entropy_check(filament) == 0.0

def test_entropy_based_primer():
    filament = ["E", "P", "S", "S"]
    primer = entropy_based_primer(filament)
    assert isinstance(primer, list)
    assert len(primer) == 4
