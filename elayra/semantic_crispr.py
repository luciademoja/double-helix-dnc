# Modulo per inserzione intenzionale di nucleotidi semantici
from elayra.abundance_reset import select_primer

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
    level = entropy_check(filament)
    if level > 0.75:
        return select_primer("exploration")
    elif level > 0.5:
        return select_primer("intuition")
    elif level > 0.25:
        return select_primer("protection")
    else:
        return select_primer("reset")