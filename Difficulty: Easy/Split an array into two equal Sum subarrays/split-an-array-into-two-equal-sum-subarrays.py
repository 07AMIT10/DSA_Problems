class Solution:
    def canSplit(self, arr):
        tSum=sum(arr)
        if tSum%2==1:
            return False
        hSum=tSum//2
        for i in range(len(arr)-1):
            hSum-=arr[i]
            if hSum==0:
                return True
        return False

#{ 
 # Driver Code Starts
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    t = int(data[0])
    index = 1
    for _ in range(t):
        arr = list(map(int, data[index].split()))
        index += 1

        obj = Solution()
        res = obj.canSplit(arr)
        if (res):
            print("true")
        else:
            print("false")

# } Driver Code Ends