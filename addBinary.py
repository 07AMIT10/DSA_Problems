class Solution:
    def addBinary(self, a: str, b: str) -> str:
        fs = str(bin(int(a,2)+int(b,2)))
        return fs[2:]

s = Solution()
print(s.addBinary('100', '11')
