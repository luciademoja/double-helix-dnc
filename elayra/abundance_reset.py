# Reset attraverso meditazione semantica
from elayra.imprint import echo_abundance

def abundance_reset():
    print("Activating abundance mantra reset...")
    print(echo_abundance)
    return select_primer("reset")


def select_primer(mode="reset"):
    primer_library = {
        "reset": ["E", "S", "E", "P"],
        "exploration": ["P", "E", "S", "P"],
        "protection": ["C", "S", "C", "P"],
        "intuition": ["E", "S", "P", "E"]
    }
    return primer_library.get(mode, ["E", "S", "E", "P"])
