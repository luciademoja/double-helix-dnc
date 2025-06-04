# ecps_interpreter.py

import datetime
import random

# Mappa binaria per la decodifica ECPS
binary_map = {
    "00": "E",  # Espansione
    "01": "C",  # Contrazione
    "10": "P",  # Percezione
    "11": "S"   # Senso
}

# Mappa delle diadi risonanti
meaning_map = {
    ("E", "P"): "Expansion outward – curiosity",
    ("E", "S"): "Expansion inward – intuition",
    ("C", "P"): "Contraction outward – defense",
    ("C", "S"): "Contraction inward – reflection"
}

# Coppie considerate inerti (non risonanti)
inert_pairs = [
    ("P", "E"), ("P", "C"), ("S", "E"), ("S", "C"),
    ("E", "E"), ("C", "C"), ("P", "P"), ("S", "S"),
    ("P", "S"), ("S", "P"), ("E", "C"), ("C", "E")
]

# Decodifica binario in simboli ECPS
def decode_binary_to_ecps(binary_string):
    pairs = [binary_string[i:i+2] for i in range(0, len(binary_string), 2)]
    return [binary_map.get(p, "?") for p in pairs]

# Interpreta il filamento in base alle diadi
# Applica mutazioni alle coppie inerti per ottenere diadi risonanti
# Ritorna interpretazioni e log delle mutazioni
def interpret_ecps(filament):
    interpretations = []
    mutation_log = []

    for i in range(len(filament) - 1):
        a, b = filament[i], filament[i+1]
        pair = (a, b)

        if pair in meaning_map:
            interpretations.append(meaning_map[pair])
        elif pair in inert_pairs:
            mutated_b = suggest_mutation(a)
            mutated_pair = (a, mutated_b)

            reason = f"{pair} is inert, mutated {b} → {mutated_b} for coherence"
            timestamp = datetime.datetime.now().isoformat()

            interpretations.append(meaning_map.get(mutated_pair, "Unknown"))
            mutation_log.append({
                "original_pair": pair,
                "mutated_pair": mutated_pair,
                "mutation_reason": reason,
                "timestamp": timestamp
            })
        else:
            interpretations.append("Unknown")

    return interpretations, mutation_log

# Suggerisce una mutazione coerente per ottenere una diade risonante
def suggest_mutation(a):
    candidates = [(x, y) for (x, y) in meaning_map if x == a]
    if not candidates:
        return a
    _, target_b = random.choice(candidates)
    return target_b
