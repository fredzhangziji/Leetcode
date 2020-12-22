class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # return str(int(num1) + int(num2))
        
        res = []
        
        # set the carry as 0 first
        carry = 0
        
        # set pointers for both string
        p1 = len(num1) - 1
        p2 = len(num2) - 1
        
        while p1 >= 0 or p2 >= 0:
            # covert x1 and x2 from string to nums without using builtin int() or str()
            x1 = ord(num1[p1]) - ord('0') if p1 >= 0 else 0
            x2 = ord(num2[p2]) - ord('0') if p2 >= 0 else 0
            
            value = (x1+x2+carry) % 10
            carry = (x1+x2+carry) // 10
            res.append(value)
            
            p1 -= 1
            p2 -= 1
        
        if carry:
            res.append(carry)
            
        
        return ''.join(str(x) for x in res[::-1])