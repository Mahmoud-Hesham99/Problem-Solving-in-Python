import random
class RandomizedSet:

    def __init__(self):
        self.data_map = {} # dictionary, map, hash table, O(1) insert, O(1) lookup
        self.data_list = [] # list/array

    def insert(self, val: int) -> bool:
        # check if val is in the dictionary
        if val in self.data_map:
            return False

        # add val to the dictionary and give it an index as last element in the list
        self.data_map[val] = len(self.data_list)

        self.data_list.append(val)
        
        return True

    def remove(self, val: int) -> bool:

        # check if val is in the dictionary
        if not val in self.data_map:
            return False

        # get the index of the val in the list so we can replace it with the last element in the list
        # then pop the last element in the list O(1) yay!
        last_elem = self.data_list[-1]
        val_index = self.data_map[val]

        self.data_map[last_elem] = val_index
        self.data_list[val_index] = last_elem

        self.data_list[-1] = val

        self.data_list.pop()

        self.data_map.pop(val)
        return True

    def getRandom(self) -> int:
        # since we have a list, we can just use random.choice to get a random element from the list O(1)
        return random.choice(self.data_list)

if __name__ == "__main__":
    
# Your RandomizedSet object will be instantiated and called as such:
    obj = RandomizedSet()
    param_1 = obj.insert(1)
    param_2 = obj.remove(2)
    param_3 = obj.insert(2)
    param_4 = obj.getRandom()
    print(param_1)
    print(param_2)
    print(param_3)
    print(param_4)