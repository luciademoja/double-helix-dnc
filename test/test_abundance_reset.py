from elayra.abundance_reset import abundance_reset, select_primer

def test_select_primer():
    assert select_primer("reset") == ["E", "S", "E", "P"]
    assert select_primer("exploration") == ["P", "E", "S", "P"]

def test_abundance_reset(monkeypatch):
    # Stub imprint.abundance_mantra
    monkeypatch.setattr("imprint.abundance_mantra", lambda: "I am abundant.")
    result = abundance_reset()
    assert result == ["E", "S", "E", "P"]
