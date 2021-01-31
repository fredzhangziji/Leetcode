class Solution:
    """
    @param reader: An instance of ArrayReader.
    @param target: An integer
    @return: An integer which is the first index of target.
    """
    def searchBigSortedArray(self, reader, target):
        # write your code here
        
        start = 0
        end = 1 
        while reader.get(end) < target:
            end *= 2 
        
        while start + 1 < end:
            mid = (start + end) // 2
            # 这里要注意，到底是小于还是小于等于。
            # 因为我们要返回第一个出现的位置，所以这边要设置成小于。
            # 如果设置成小于等于，那么有可能恰好mid指向了 5 5 5 这三个数的中间那个5，那么就错了。
            if reader.get(mid) < target:
                start = mid 
            else:
                end = mid
        
        if reader.get(start) == target:
            return start
        elif reader.get(end) == target:
            return end
        else:
            return -1 