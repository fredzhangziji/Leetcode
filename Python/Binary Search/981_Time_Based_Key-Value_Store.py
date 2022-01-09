import collections
import bisect

class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.M = collections.defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.M[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        A = self.M.get(key,None)
        if A is None:
            return ""
        i = bisect.bisect(A, (timestamp, chr(127)))
        return A[i-1][1] if i else ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)