import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.randomSet = set()

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.randomSet:
            return False
        else:
            self.randomSet.add(val)
            return True
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.randomSet:
            return False
        else:
            self.randomSet.remove(val) 
            return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        
        return random.choice(tuple(self.randomSet))


# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
param_1 = obj.insert(1)
param_2 = obj.remove(2)
param_3 = obj.getRandom()
print(param_3)
