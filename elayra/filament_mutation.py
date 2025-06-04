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

def mutate_filament(filament):
    mutated = filament[:]
    mutation_log = []

    for i in range(len(filament) - 1):
        pair = (filament[i], filament[i + 1])

        if pair in resonant_pairs:
            continue  # già risonante

        original = pair
        mutation_attempts = 0
        reason = ""

        # tenta di mutare il secondo elemento finché non ottiene una coppia risonante
        options = ["E", "C", "P", "S"]
        for replacement in options:
            candidate = (filament[i], replacement)
            mutation_attempts += 1
            if candidate in resonant_pairs:
                mutated[i + 1] = replacement
                reason = f"Mutated {original} to {candidate} after {mutation_attempts} attempts for resonance"
                break

        if reason:
            mutation_log.append({
                "index": i,
                "original_pair": original,
                "mutated_pair": (filament[i], mutated[i + 1]),
                "mutation_reason": reason,
                "timestamp": datetime.datetime.now().isoformat()
            })

    return mutated, mutation_log

def log_mutations_to_file(mutation_log, path="elayra/mutation_log.json"):
    import os, json
    os.makedirs(os.path.dirname(path), exist_ok=True)
    try:
        with open(path, "a") as f:
            for entry in mutation_log:
                f.write(json.dumps(entry) + "\n")
    except Exception as e:
        print("Logging error (mutation log):", e)
