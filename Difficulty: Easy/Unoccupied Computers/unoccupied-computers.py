class Solution:
    def solve(self, n, s):
        # code here
        vis = {}
        cnt = 0
        for i in s:
    
            if i not in vis:
                if n:
                    n -= 1
                    vis[i]=1
                else:
                    cnt += 1
                    vis[i] = 0
            else:
                if vis[i] == 1:
                    n += 1
                del vis[i]
    
    
        return cnt