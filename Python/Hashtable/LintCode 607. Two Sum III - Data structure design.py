class TwoSum:
    
    # define the data structure here
    def __init__(self):
        self.count = {}
    
    """
    @param number: An integer
    @return: nothing
    """
    def add(self, number):
        # write your code here
        if number in self.count:
            self.count[number] += 1 
        else:
            self.count[number] = 1 
        
    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    def find(self, value):
        # write your code here
        for num in self.count:
            if value - num in self.count:
                if value - num == num and self.count[value - num] > 1:
                    return True
                elif value - num != num:
                    return True
                else:
                    continue
            else:
                continue
            
        return False