#User function Template for python3
# POTD FOR JUNE 4
class Solution:
	def binaryNextNumber(self, s):
		# code here
		s = int(s, 2)
		s+=1
		return bin(s)[2:]
		

sol = Solution()
print(sol.binaryNextNumber('10'))
