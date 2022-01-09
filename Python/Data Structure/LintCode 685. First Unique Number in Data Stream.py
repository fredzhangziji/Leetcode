class Solution:
    """
    @param nums: a continuous stream of numbers
    @param number: a number
    @return: returns the first unique number
    """
    def firstUniqueNumber(self, nums, number):
        # Write your code here
        counter = {}
        for num in nums:
            # this section can be rewritten as:
            # counter[num] = counter.get(num, 0) + 1
            if num not in counter:
                counter[num] = 1
            else:
                counter[num] += 1

            if num == number:
                break
        # for-else structure:
        # When you search something in the for loop, when you find it, you break, and it won't enter
        # the else clause;
        # When you don't find it, the for loop ends completely, it will enter the else clause.
        # In a word: if we break -> no else;
        #            if we end full for loop -> else
        else:
            return -1
        
        for num in nums:
            if counter[num] == 1:
                return num
        
        return -1