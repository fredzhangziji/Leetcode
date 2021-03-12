class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySum(self, nums):
        # write your code here
        # O(n^2)
        # length = len(nums)
        # for i in range(length):
        #     if nums[i] == 0:
        #         return [i, i]
        #     currSum = nums[i]
        #     for j in range(i + 1, length):
        #         currSum += nums[j]
        #         if currSum == 0:
        #             return [i, j]

        # O(n): prefix sum
        hashset = {0: -1}
        result = []
        sums = 0
        for i, num in enumerate(nums):
            sums += num
            if sums in hashset:
                result.append(hashset[sums] + 1)
                result.append(i)
                return result
            
            hashset[sums] = i
