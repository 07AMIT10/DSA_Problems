#User function Template for python3
class Solution:
	def bracketNumbers(self, str):
	    ans = []
	    opening_bracket_num = 1
	    closing_bracket_num = 1
	    closed_taken = set()
	    
	    for ch in str:
	        if ch == '(':
	            ans.append(opening_bracket_num)
	            closing_bracket_num = opening_bracket_num
	            opening_bracket_num += 1
	        elif ch == ')':
	            while closing_bracket_num in closed_taken:
	                closing_bracket_num -= 1
	            ans.append(closing_bracket_num)
	            closed_taken.add(closing_bracket_num)
	            closing_bracket_num -= 1
	    
	    return ans
