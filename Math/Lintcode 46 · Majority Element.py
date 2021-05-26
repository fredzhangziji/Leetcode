# Boyer–Moore majority vote algorithm
class Solution:
    """
    @param: nums: a list of integers
    @return: find a  majority number
    """
    def majorityNumber(self, nums):
        # write your code here
        
        storedNum = None
        count = 1
        for num in nums:
            if num == storedNum:
                count += 1
            else:
                count -= 1
                if count == 0:
                    storedNum = num
                    count = 1
        
        return storedNum
