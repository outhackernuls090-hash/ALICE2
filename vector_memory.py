from config import CONFIG

class VectorMemory:
    def __init__(self):
        self.memory = []

    def add(self, item):
        if len(self.memory) >= CONFIG['memory_size']:
            self.memory.pop(0)
        self.memory.append(item)
        return item

    def search(self, query):
        return [item for item in self.memory if query.lower() in item.lower()]
