# index.py
# Ponte tra DNC neurale (es. ixaxaar/pytorch-dnc) e simbolico ECPS + mutazioni loggate

from dnc.dnc import DNC  # da repo neurale
from elayra.filament_mutation import mutate_filament
import torch
import torch.nn as nn
import json
import datetime
import os


def process_through_symbolic(binary_input):
    # Assicura che la stringa binaria abbia lunghezza pari
    if len(binary_input) % 2 != 0:
        binary_input = binary_input[:-1]

    mutated_filament, interpretation, mutation_log = mutate_filament(binary_input)

    log = {
        "timestamp": datetime.datetime.now().isoformat(),
        "input": binary_input,
        "mutated_filament": mutated_filament,
        "interpretation": interpretation,
        "mutation_log": mutation_log
    }

    os.makedirs("elayra", exist_ok=True)
    try:
        with open("elayra/resonant_memory.json", "a") as f:
            f.write(json.dumps(log) + "\n")
    except Exception as e:
        print("Logging error:", e)

    return mutated_filament, interpretation


def run_with_dnc():
    model = DNC(
        input_size=10,  # Placeholder, da adattare al tuo use case
        hidden_size=64,
        rnn_type='lstm',
        num_layers=1,
        nr_cells=16,
        cell_size=16,
        read_heads=1,
        batch_first=True
    )
    model.eval()

    dummy_input = torch.randn(1, 5, 10)  # batch x seq x input_dim
    batch_size = dummy_input.size(0)

    # Stato iniziale per DNC
    hx = model._init_hidden(None, batch_size=batch_size, reset_experience=True)

    with torch.no_grad():
        output, _ = model(dummy_input, hx)

    print("DNC Neural Output:", output)


if __name__ == "__main__":
    binary = "00101111"  # E, P, S, S
    filament, interpretation = process_through_symbolic(binary)
    print("Filament Interpretation:", interpretation)

    run_with_dnc()
