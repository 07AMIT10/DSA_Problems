#User function Template for python3

class Solution:
    def Maximize(self, arr): 
        # Complete the function
        MOD = 10**9+7
        arr = sorted(arr)
        res = 0
        for i in range(len(arr)):
            res = res+ i*arr[i]
        return res%MOD



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        A = list(map(int, input().strip().split()))
        # k = int(input())
        ob = Solution()
        print(ob.Maximize(A))

# } Driver Code Ends