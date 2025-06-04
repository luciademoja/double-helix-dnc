# semantic_crispr.py

import datetime
import random

# Mappa delle diadi risonanti
resonant_pairs = {
    ("E", "P"): "Expansion outward – curiosity",
    ("E", "S"): "Expansion inward – intuition",
    ("C", "P"): "Contraction outward – defense",
    ("C", "S"): "Contraction inward – reflection"
}

# Diadi considerate inerti (non risonanti)
inert_pairs = [
    ("P", "E"), ("P", "C"), ("S", "E"), ("S", "C"),
    ("E", "E"), ("C", "C"), ("P", "P"), ("S", "S"),
    ("P", "S"), ("S", "P"), ("E", "C"), ("C", "E")
]

def crispr_insert(filament, intention_nucleotide, position):
    if position < 0 or position > len(filament):
        raise ValueError("Invalid position")
    return filament[:position] + [intention_nucleotide] + filament[position:]

def entropy_check(filament):
    from collections import Counter
    counter = Counter(filament)
    max_freq = max(counter.values())
    return 1 - (max_freq / len(filament))  # entropy level (0 to ~1)

def entropy_based_primer(filament):
    options = ["E", "C", "P", "S"]
    primer = []
    for _ in range(4):
        primer.append(random.choice(options))
    return primer
