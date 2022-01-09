class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        # write your code here
        
        # 这个hashtable的key就是数组里面的值，value就是这个值在原数组里面对应的index
        hashtable = {}
        
        for i in range(len(numbers)):
            # 如果这个key存在于hashtable里，就直接返回这个key的index和当前数字的index
            if target - numbers[i] in hashtable:
                return [hashtable[target - numbers[i]], i]
            
            # 如果这个key不在hashtable里，就把这个key（的值）和他的index存进hashtable里
            else:
                hashtable[numbers[i]] = i
            
        return [-1, -1]