# from collections import List

class Solution:
    def threeSum(self, nums):
        target = []
        nums.sort()
        for i in range(len(nums)):
            l = i+1
            r = len(nums)-1
            while l<r:
                if nums[l]==nums[l+1]:
                    # continue
                    l+=2
                elif (nums[i]+nums[l]+nums[r]<0):
                    l+=1
                elif (nums[i]+nums[l]+nums[r]>0):
                    r-=1
                else:
                    target.append([nums[i],nums[l], nums[r]])
                    # l+=1
                    # while nums[l]==nums[l-1] and l<r:
                    #     l+=1
        return target
    
ob = Solution()
print(ob.threeSum([-1,0,1,2,-1,-4]))