class RandomizedSet:

    def __init__(self):
        self.hash_map = {}
        self.l = []
        

    def insert(self, val: int) -> bool:
        if val in self.hash_map:
            return False

        self.hash_map[val] = len(self.l)
        self.l.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.hash_map:
            return False

        list_idx = self.hash_map[val]
        last_val = self.l[-1]
        self.l[list_idx] = last_val
        self.l.pop()
        self.hash_map[last_val] = list_idx
        del self.hash_map[val]

        return True

        

    def getRandom(self) -> int:
        # rand_idx = random.randint(0, len(self.l) - 1)
        # return self.l[rand_idx]
        return random.choice(self.l)

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()