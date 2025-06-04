import json
import datetime
import os


class MemoryManager:
    def __init__(self, path='elayra/memory_store.json'):
        self.path = path
        self.data = []
        self.load()

    def load(self):
        """Carica la memoria dal file JSON se esiste, altrimenti inizializza vuoto."""
        if not os.path.exists(self.path):
            self.data = []
            return
        try:
            with open(self.path, 'r', encoding='utf-8') as f:
                self.data = json.load(f)
        except json.JSONDecodeError:
            print(f"⚠️  Warning: {self.path} non è un JSON valido. Resetting memory.")
            self.data = []

    def save(self):
        """Scrive il contenuto attuale della memoria nel file."""
        os.makedirs(os.path.dirname(self.path), exist_ok=True)
        with open(self.path, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, indent=2, ensure_ascii=False)

    def save_memory(self, filament, context="", entropy=None, mutation_log=None):
        """Aggiunge un nuovo evento alla memoria e salva su file."""
        entry = {
            'timestamp': datetime.datetime.now().isoformat(),
            'filament': filament,
            'context': context,
            'entropy': entropy,
        }
        if mutation_log:
            entry['mutation_log'] = mutation_log
        self.data.append(entry)
        self.save()

    def recall_by_cue(self, cue):
        """Restituisce tutte le memorie che contengono un determinato cue nel campo 'context'."""
        return [entry for entry in self.data if cue in entry.get('context', '')]

    def last(self, n=1):
        """Recupera gli ultimi n elementi dalla memoria."""
        return self.data[-n:]
