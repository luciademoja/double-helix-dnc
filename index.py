# index.py interattivo

from elayra.ecps_interpreter import decode_binary_to_ecps, interpret_ecps
from elayra.filament_mutation import mutate_filament
from elayra.semantic_crispr import entropy_check, entropy_based_primer
from elayra.abundance_reset import abundance_reset
import datetime, json, os
import random

def generate_sequence(primer, target_length=100):
    filament = primer[:]
    while len(filament) < target_length:
        next_base = random.choice(["E", "C", "P", "S"])
        filament.append(next_base)
    return filament

def start_dialogue():
    print("🌿 ECPS Symbolic Filament Generator 🌿")
    print("Inserisci un primer simbolico separato da spazi (es: E P S C), oppure premi INVIO per usare un primer casuale:")
    
    user_input = input("> ").strip().upper()
    
    if user_input:
        primer = user_input.split()
    else:
        primer = entropy_based_primer(["E", "P", "C", "S"])

    print(f"\nPrimer iniziale: {primer}")
    
    full_filament = generate_sequence(primer)
    entropy = entropy_check(full_filament)
    
    print(f"Entropy finale del filamento: {entropy:.2f}")
    
    mutated, mutation_log = mutate_filament(full_filament)
    interpretation, _ = interpret_ecps(mutated)

    # Log
    log = {
        "timestamp": datetime.datetime.now().isoformat(),
        "primer": primer,
        "filament": full_filament,
        "mutated_filament": mutated,
        "interpretation": interpretation,
        "mutation_log": mutation_log
    }

    os.makedirs("elayra", exist_ok=True)
    with open("elayra/resonant_memory.json", "a") as f:
        f.write(json.dumps(log) + "\n")

    print("\n🧬 Filamento simbolico:")
    print(" ".join(full_filament))
    print("\n🔮 Interpretazione (diadi):")
    for meaning in interpretation:
        print(" -", meaning)

if __name__ == "__main__":
    start_dialogue()
