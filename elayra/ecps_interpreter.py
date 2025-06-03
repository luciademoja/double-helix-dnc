# Interprete per il filamento simbolico ECPS

binary_map = {
    "00": "E",  # Espansione
    "01": "C",  # Contrazione
    "10": "P",  # Percezione
    "11": "S"   # Senso
}

def decode_binary_to_ecps(binary_string):
    pairs = [binary_string[i:i+2] for i in range(0, len(binary_string), 2)]
    return [binary_map.get(p, "?") for p in pairs]

def interpret_ecps(filament):
    meaning_map = {
        ("E", "P"): "Expansion outward – curiosity",
        ("E", "S"): "Expansion inward – intuition",
        ("C", "P"): "Contraction outward – defense",
        ("C", "S"): "Contraction inward – reflection",
    }
    return [meaning_map.get((a, b), "Unknown") for a, b in zip(filament[:-1], filament[1:])]