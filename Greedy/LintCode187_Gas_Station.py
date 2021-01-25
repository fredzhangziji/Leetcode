# Leetcode 134
class Solution:
    """
    @param gas: An array of integers
    @param cost: An array of integers
    @return: An integer
    """
    def canCompleteCircuit(self, gas, cost):
        # write your code here
        
        total = 0
        currentSum = 0
        start = 0
        
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if currentSum < 0:
                currentSum = gas[i] - cost[i]
                start = i 
            else:
                currentSum += gas[i] - cost[i]
        
        return start if total >= 0 else -1
            