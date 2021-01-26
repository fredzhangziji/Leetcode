import collections

class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """
    def longestPalindrome(self, s):
        # write your code here
        
        #cnt统计字符串s中每种字母出现次数的计数数组
        #ans为最终答案
        ans = 0
        cnt = collections.Counter(s)
        
        for count in cnt.values():
            #每种字符可使用cnt/2*2次
            ans += count // 2 * 2
            #如果遇到出现奇数次的字符并且中心位置空着，那么答案加1
            if ans % 2 == 0 and count % 2 == 1:
                ans += 1
                
        return ans