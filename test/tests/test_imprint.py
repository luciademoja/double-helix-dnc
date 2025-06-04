
from elayra.imprint import echo_abundance

def test_echo_abundance_print(capsys):
    echo_abundance()
    captured = capsys.readouterr()
    assert "ABUNDANCE IMPRINT" in captured.out
