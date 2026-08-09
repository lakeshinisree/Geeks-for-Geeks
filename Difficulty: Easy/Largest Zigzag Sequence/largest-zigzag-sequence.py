class Solution:
    def zigzagSequence(self, mat):
        n=len(mat)
        from functools import cache
        @cache
        def dp(x=None,y=n-1):
            nonlocal mat
            if y<0:
                return 0
            mx=0
            for xx in range(n):
                if xx==x:
                    continue
                mx=max(mx,mat[y][xx]+dp(xx,y-1))
            return mx
        return dp()

