# Orchestratore principale del sistema DNC simbolico
import datetime
from elayra.ecps_interpreter import decode_binary_to_ecps, interpret_ecps
from elayra.semantic_crispr import crispr_insert, entropy_check, entropy_based_primer
from elayra.abundance_reset import abundance_reset
import json


def process_input(binary_string):
    filament = decode_binary_to_ecps(binary_string)
    entropy = entropy_check(filament)
    print(f"Entropy level: {entropy:.2f}")

    if entropy > 0.85:
        primer = abundance_reset()
    else:
        primer = entropy_based_primer(filament)

    combined = primer + filament
    interpretations = interpret_ecps(combined)
    
    log = {
        "timestamp": datetime.datetime.now().isoformat(),
        "input": binary_string,
        "decoded": filament,
        "primer": primer,
        "combined": combined,
        "interpretation": interpretations
    }

    with open("resonant_memory.json", "a") as f:
        f.write(json.dumps(log) + "\n")

    return interpretations


# Esempio di esecuzione
if __name__ == "__main__":
    binary_input = "00101111"  # esempio: E, P, S, S
    result = process_input(binary_input)
    print("Interpretation:", result)