class HashTable:
    def __init__(self, length = 10):
        self.size = length
        self.table = [[] for _ in range(self.size)]
    
    def _hash(self, key):
        return key % self.size

    def set(self, key, value):
        index = self._hash(key)
        # Chaining
        self.table[index].append((key, value))
    
    def get(self, key):
        index = self._hash(key)
        value = self.table[index]
        
        if not value:
            return None
        for v in value:
            if v[0] == key:
                return v[1]
        return None