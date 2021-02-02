import collections

class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """
    def ladderLength(self, start, end, dict):
        # write your code here
        
        dict.add(end)
        wordLength = len(start) # 获得所有单词的长度
        queue = collections.deque([(start, 1)]) 
        # 队列中存（节点，路径长度）, 不然没法处理每次不同变化单词的长度
        
        while queue:
            curr = queue.popleft()
            currWord = curr[0]
            pathLength = curr[1]
            if currWord == end: # 每次pop掉这个单词先检查是不是end，如果是，直接返回pathlength
                return pathLength
            
            # bfs
            # 如果不是，开始替换字母，检查是不是在dict里面
            for i in range(wordLength):
                # 要替换第i个字母，那么要表示i左边和i右边
                leftHalf = currWord[:i]
                rightHalf = currWord[i+1:]
                for replacement in "abcdefghijklmnopqrstuvwxyz":
                    if currWord[i] != replacement: # 不能替换一样的字母，不然没意义了
                        newWord = leftHalf + replacement + rightHalf
                        if newWord in dict: # 如果在dict里面
                            queue.append((newWord, pathLength + 1))
                            # 如果已经转换成过这个单词，最短路径不可能再次转换到这个单词，所以直接删除dict里的
                            # 这个单词。这个操作相当于其他bfs题目里面的更新visited
                            dict.remove(newWord) 
            
        # 如果while结束了，所有单词都被访问过了，但是还是没有return，那么说明不能转换到end
        return 0