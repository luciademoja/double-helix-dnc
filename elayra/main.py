# Orchestratore principale del sistema DNC simbolico

import datetime
from elayra.ecps_interpreter import decode_binary_to_ecps, interpret_ecps
from elayra.semantic_crispr import crispr_insert, entropy_check, entropy_based_primer
from elayra.abundance_reset import abundance_reset
import json, os


def process_input(binary_string):
    # Troncamento per sicurezza se lunghezza binaria dispari
    if len(binary_string) % 2 != 0:
        binary_string = binary_string[:-1]

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

    os.makedirs("elayra", exist_ok=True)
    try:
        with open("elayra/resonant_memory.json", "a") as f:
            f.write(json.dumps(log) + "\n")
    except Exception as e:
        print("Logging error:", e)

    return interpretations


# Esecuzione autonoma
if __name__ == "__main__":
    binary_input = "00101111"
    result = process_input(binary_input)
    print("Interpretation:", result)
