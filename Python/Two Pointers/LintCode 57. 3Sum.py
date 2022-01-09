class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        # write your code here
        
        numbers.sort()
        res = []
        for i in range(len(numbers)):
            if i > 0 and numbers[i] == numbers[i - 1]:
                continue
            
            self.twoSum(numbers, -numbers[i], i + 1, len(numbers) - 1, res)
            
        return res
        
    
    
    def twoSum(self, numbers, target, left, right, res):
        lastPair = None
        while left < right:
            if numbers[left] + numbers[right] == target and (numbers[left], numbers[right]) != lastPair:
                res.append([-target, numbers[left], numbers[right]])
                lastPair = (numbers[left], numbers[right])
                left += 1 
                right -= 1 
            elif numbers[left] + numbers[right] < target:
                left += 1 
            else:
                right -= 1 
                
        return res
            