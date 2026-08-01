class Solution:
    def findMax(self, n, a, b, k):
        inc=[0]*n
        for ix in range(len(a)):
            inc[a[ix]]+=k[ix]
            if b[ix]+1<n:
                inc[b[ix]+1]-=k[ix]
        mx=inc[0]
        for ix in range(1,n):
            inc[ix]+=inc[ix-1]
            mx=max(mx,inc[ix])
        return mx