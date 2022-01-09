class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if a == "0" and b == "0":
            return "0"
            
        def biToDeci(z):
            sumz = z % 2
            z = z//10
            count = 1
            while z > 0:
                sumz += (2**count) * (z % 2)
                z = z // 10
                count += 1
            return sumz
        
        def deciToBi(z):
            sumz = ""
            while z > 0:
                sumz += str(z % 2)
                z = z // 2
            return int(sumz[::-1])
        
        print(biToDeci(int(a)))
        print(biToDeci(int(b)))

        return str(deciToBi(biToDeci(int(a)) + biToDeci(int(b))))
        