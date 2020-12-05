from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
#         如果用brute force，O(n^2)，会超时
#         res = []
#         for i in range(len(nums)):
#             res.append(1)
#             for j in range(len(nums)):
#                 if i != j:
#                     res[i] *= nums[j]
        
#         return res


        # 统计0的个数
        zeroCount = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zeroCount += 1
        # 如果0的个数大于等于2，那么结果肯定都是0
        if zeroCount >= 2:
            return [0] * len(nums)

        # 如果0的个数小于2，那么就开始计算
        # 先算出所有数的积，然后除以当前的element，这样的话时间复杂度只有O(n)
        res1 = 1
        for i in range(len(nums)):
            if nums[i] != 0:
                res1 *= nums[i]
        res= [res1]*len(nums)
        
        # 如果有0（只有一个0），那么除了0这个index的积是有的，另外的index都是0
        if 0 in nums:
            for i in range(len(nums)):
                if nums[i] != 0:
                    res[i] = 0 
        # 没有0就正常算
        else:
            for i in range(len(nums)):
                res[i] = int(res[i] / nums[i])
            
        return res