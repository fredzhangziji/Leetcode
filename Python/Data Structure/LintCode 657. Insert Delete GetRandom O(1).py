import random

class RandomizedSet:
    
    def __init__(self):
        # do intialization if necessary
        # store in an array
        self.num = []
        # store the index in a dictionary
        self.val2idx = {}

    """
    @param: val: a value to the set
    @return: true if the set did not already contain the specified element or false
    """
    def insert(self, val):
        # write your code here
        if val in self.num:
            return False
        else:
            self.num.append(val)
            self.val2idx[val] = len(self.num) - 1
            return True

    """
    @param: val: a value from the set
    @return: true if the set contained the specified element or false
    """
    def remove(self, val):
        # write your code here
        if val not in self.num:
            return False
        else:
            idx = self.val2idx[val]
            last = self.num[-1]
            self.num[idx] = last
            self.val2idx[last] = idx 
            self.num.pop()
            del self.val2idx[val]
            return True

    """
    @return: Get a random element from the set
    """
    def getRandom(self):
        # write your code here
        return self.num[random.randint(0, len(self.num) - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param = obj.insert(val)
# param = obj.remove(val)
# param = obj.getRandom()