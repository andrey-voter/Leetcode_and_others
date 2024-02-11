import random


class RandomizedSet:

    def __init__(self):
        self.index_dict = {}
        self.help_list = []

    def insert(self, val: int) -> bool:
        if val in self.index_dict:
            return False
        self.help_list.append(val)
        self.index_dict[val] = len(self.help_list) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.index_dict:
            return False
        index = self.index_dict[val]
        self.help_list[index], self.help_list[-1] = self.help_list[-1], self.help_list[index]
        self.index_dict[self.help_list[index]] = index
        self.help_list.pop()
        del self.index_dict[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.help_list)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
