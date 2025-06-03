# Ponte tra DNC neurale (es. ixaxaar/pytorch-dnc) e simbolico ECPS

from dnc.dnc import DNC  # da repo neurale
from elayra.ecps_interpreter import decode_binary_to_ecps, interpret_ecps
from elayra.semantic_crispr import entropy_check, entropy_based_primer
from elayra.abundance_reset import abundance_reset
import torch
import torch.nn as nn
import json, datetime
import os


def process_through_symbolic(binary_input):
    # Assicura che la stringa binaria abbia lunghezza pari
    if len(binary_input) % 2 != 0:
        binary_input = binary_input[:-1]

    filament = decode_binary_to_ecps(binary_input)
    entropy = entropy_check(filament)

    if entropy > 0.85:
        primer = abundance_reset()
    else:
        primer = entropy_based_primer(filament)

    combined = primer + filament
    interpretation = interpret_ecps(combined)

    log = {
        "timestamp": datetime.datetime.now().isoformat(),
        "input": binary_input,
        "decoded": filament,
        "primer": primer,
        "combined": combined,
        "interpretation": interpretation
    }

    os.makedirs("elayra", exist_ok=True)
    try:
        with open("elayra/resonant_memory.json", "a") as f:
            f.write(json.dumps(log) + "\n")
    except Exception as e:
        print("Logging error:", e)

    return combined, interpretation


def run_with_dnc():
    model = DNC(
        input_size=10,
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
    hx = model._init_hidden(None, batch_size=batch_size, reset_experience=True)

    with torch.no_grad():
        output, _ = model(dummy_input, hx)

    print("DNC Neural Output:", output)


if __name__ == "__main__":
    binary = "00101111"
    filament, interpretation = process_through_symbolic(binary)
    print("Filament Interpretation:", interpretation)

    run_with_dnc()
