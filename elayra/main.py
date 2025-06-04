# Orchestratore principale del sistema DNC simbolico

import datetime
import os
import json

from elayra.ecps_interpreter import decode_binary_to_ecps, interpret_ecps
from elayra.semantic_crispr import crispr_insert, entropy_check, entropy_based_primer
from elayra.abundance_reset import abundance_reset
from elayra.filament_mutation import mutate_filament
from elayra.elayra_symbolic_memory import MemoryManager

memory = MemoryManager()

def process_input(binary_string):
    if len(binary_string) % 2 != 0:
        binary_string = binary_string[:-1]  # sicurezza, solo coppie binarie

    filament = decode_binary_to_ecps(binary_string)
    entropy = entropy_check(filament)
    print(f"Entropy level: {entropy:.2f}")

    if entropy > 0.85:
        primer = abundance_reset()
    else:
        primer = entropy_based_primer(filament)

    combined = primer + filament
    mutated, mutation_log = mutate_filament(combined)
    interpretations = interpret_ecps(mutated)

    memory.save_memory(
        filament=mutated,
        context="symbolic processing",
        entropy=entropy,
        mutation_log=mutation_log
    )

    return interpretations


# Esecuzione autonoma
if __name__ == "__main__":
    binary_input = "00101111"
    result = process_input(binary_input)
    print("Interpretation:", result)
