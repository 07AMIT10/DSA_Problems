class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0,0
        maxl = 0
        stl=""
        while r<len(s):
            if s[r] not in stl:
                stl+=s[r]
                r+=1
            else:
                stl = max(stl, s[l:r+1])
                l = r
            r+=1
                
        return len(stl)

        


a = Solution()
print(a.lengthOfLongestSubstring("aabcabdd"))