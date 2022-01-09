from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 这题相当于用python的sort作弊了
        # 应该是要用binary sort或者insertion sort来做
        nums3 = nums1 + nums2
        nums3.sort()
        if len(nums3) % 2 == 0:
            return (nums3[int(len(nums3)/2)] + nums3[int(len(nums3)/2)-1]) / 2
        if len(nums3) % 2 == 1:
            return nums3[int((len(nums3)-1)/2)]
                                                  