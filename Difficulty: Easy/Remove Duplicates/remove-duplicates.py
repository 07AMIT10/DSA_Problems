class Solution:
    def removeDups(self, str):
        s1=''
        for i in str:
            if i not in s1:
                s1+=i
        return s1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s = input()

        ob = Solution()
        answer = ob.removeDups(s)

        print(answer)

# } Driver Code Ends