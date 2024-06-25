class Solution:
    def reverse(self,arr,s,e):
        while s<e:
            arr[s],arr[e]=arr[e],arr[s]
            s+=1
            e-=1
    
    def rotateMatrix(self, k, mat):
        r,c=len(mat),len(mat[0])
        k=k%c
        for i in range(r):
            self.reverse(mat[i],0,k-1)
            self.reverse(mat[i],k,c-1)
            self.reverse(mat[i],0,c-1)
        return mat
