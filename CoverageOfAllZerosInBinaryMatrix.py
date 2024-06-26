#User function Template for python3
class Solution:
	def findCoverage(self, matrix):
		# Code here
        
        n = len(matrix)
        m = len(matrix[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        def isValid(x,y):
            return x>=0 and y>=0 and x<n and y<m
        c = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    for [x,y] in directions: 
                        if isValid(i+x,j+y) and matrix[i+x][j+y]==1:
                            c+=1                        
        
        return c
