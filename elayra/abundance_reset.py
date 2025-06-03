# Reset attraverso meditazione semantica
import imprint
from elayra.semantic_crispr import select_primer

def abundance_reset():
    print("Activating abundance mantra reset...")
    print(imprint.abundance_mantra())
    return select_primer("reset")


def select_primer(mode="reset"):
    primer_library = {
        "reset": ["E", "S", "E", "P"],
        "exploration": ["P", "E", "S", "P"],
        "protection": ["C", "S", "C", "P"],
        "intuition": ["E", "S", "P", "E"]
    }
    return primer_library.get(mode, ["E", "S", "E", "P"])
