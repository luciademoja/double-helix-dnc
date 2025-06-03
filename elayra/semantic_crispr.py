# Modulo per inserzione intenzionale di nucleotidi semantici

def crispr_insert(filament, intention_nucleotide, position):
    if position < 0 or position > len(filament):
        raise ValueError("Invalid position")
    return filament[:position] + [intention_nucleotide] + filament[position:]


def entropy_check(filament):
    from collections import Counter
    counter = Counter(filament)
    max_freq = max(counter.values())
    return 1 - (max_freq / len(filament))  # entropy level (0 to ~1)
