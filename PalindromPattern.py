#User function Template for python3

class Solution:
    def pallindrome(self,arr, n):
        for i in range(n):
            if arr[i] != arr[n - i - 1]:
                return False
        return True

    def pattern(self, arr):
        n = len(arr)
        ans = "-1"
        
        # Check rows
        for i in range(n):
            curr_row = arr[i]
            if self.pallindrome(curr_row, n):
                ans = "{} R".format(i)
                return ans
        
        # Check columns
        for j in range(n):
            curr_col = [arr[i][j] for i in range(n)]
            if self.pallindrome(curr_col, n):
                ans = "{} C".format(j)
                return ans
        
        return ans





#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    ob = Solution()
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        a = list()
        c = 0
        for i in range(0, n):
            X = list()
            for j in range(0, n):
                X.append(arr[c])
                c += 1
            a.append(X)
        ans = ob.pattern(a)
        print(ans)

# } Driver Code Ends
