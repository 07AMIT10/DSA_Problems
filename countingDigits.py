
class Solution:
    def evenlyDivides (self, n):
        num = str(n)
        cnt=0
        for i in num:
            if int(i)==0:
                continue
            elif n%int(i)==0:
                cnt+=1
               
            
        return cnt


