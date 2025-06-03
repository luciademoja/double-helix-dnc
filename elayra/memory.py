import json

class MemoryManager:
    def __init__(self, path='memory_store.json'):
        self.path = path
        self.load()

    def load(self):
        try:
            with open(self.path, 'r') as f:
                self.data = json.load(f)
        except:
            self.data = []

    def save_memory(self, filament, context, entropy):
        self.data.append({'filament': filament, 'context': context, 'entropy': entropy})
        with open(self.path, 'w') as f:
            json.dump(self.data, f, indent=2)

    def recall_by_cue(self, cue):
        return [entry for entry in self.data if cue in entry['context']]
