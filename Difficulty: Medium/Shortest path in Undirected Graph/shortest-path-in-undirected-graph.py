#User function Template for python3
from collections import deque
class Solution:
    def shortestPath(self, edges, n, m, src):
        adj=[[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        q=deque()
        visited=[False]*n
        q.append(src)
        visited[src]=True
        distance=[-1]*n
        level=0
        while q:
            for _ in range(len(q)):
                u=q.popleft()
                distance[u]=level
                for v in adj[u]:
                    if visited[v]==False:
                        q.append(v)
                        visited[v]=True
            level+=1
        return distance

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, m = map(int, input().strip().split())
        edges=[]
        for i in range(m):
            li=list(map(int,input().split()))
            edges.append(li)
        src=int(input())
        ob = Solution()
        ans = ob.shortestPath(edges,n,m,src)
        for i in ans:
            print(i,end=" ")
        print()
        tc -= 1
# } Driver Code Ends