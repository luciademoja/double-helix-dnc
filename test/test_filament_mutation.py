
import pytest
from elayra.filament_mutation import mutate_filament

def test_mutate_filament_output():
    filament = ["P", "E", "E", "S"]
    mutated, log = mutate_filament(filament)
    assert isinstance(mutated, list)
    assert isinstance(log, list)
