from elayra.ecps_interpreter import decode_binary_to_ecps, interpret_ecps

def test_decode_binary_to_ecps():
    assert decode_binary_to_ecps("00101111") == ["E", "P", "S", "S"]

def test_interpret_ecps():
    filament = ["E", "P", "S", "S"]
    result = interpret_ecps(filament)
    assert result == ["Expansion outward – curiosity", "Unknown", "Unknown"]
