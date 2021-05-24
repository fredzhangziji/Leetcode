PI = 3.14
class Solution:
    """
    @param r: a Integer represent radius
    @return: the circle's circumference nums[0] and area nums[1]
    """
    def calculate(self, r):
        # write your code here
        return [2*r*PI, r*r*PI]