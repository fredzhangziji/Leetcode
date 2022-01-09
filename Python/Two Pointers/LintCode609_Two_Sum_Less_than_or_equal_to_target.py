class Solution:
    """
    @param nums: an array of integer
    @param target: an integer
    @return: an integer
    """
    def twoSum5(self, nums, target):
        # write your code here
        
        nums.sort()
        
        start = 0
        end = len(nums) - 1 
        ans = 0
        
        while start < len(nums) - 1:
            while nums[start] + nums[end] > target and end >= 0:
                end -= 1 
            
            if end > start:
                ans += end - start
                
            else:
                break
            
            start += 1 
            
        return ans