
import pytest
from elayra.ecps_interpreter import decode_binary_to_ecps, interpret_ecps

def test_decode_binary_to_ecps():
    result = decode_binary_to_ecps("00101111")
    assert result == ["E", "P", "S", "S"]

def test_interpret_ecps_mutation_log():
    interpretations, log = interpret_ecps(["P", "E", "C", "S"])
    assert isinstance(interpretations, list)
    assert isinstance(log, list)
