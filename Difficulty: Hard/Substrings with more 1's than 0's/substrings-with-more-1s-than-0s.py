class BITree:
    def __init__(self, n):
        self.arr = [0]*(n+1)
        
    def update(self, i, e):
        i += 1
        while i < len(self.arr):
            self.arr[i] += e
            i += i&-i
            
    def query(self, i):
        i += 1
        r = 0
        while i > 0:
            r += self.arr[i]
            i -= i&-i
        return r
        
class Solution:
    def countSubstring(self, s):
        # code here
        arr = [0]*len(s)
        r = 0
        minv, maxv = 0, 0          # seed with pref[0]=0 instead of ±inf
        for i, e in enumerate(s):
            r += -1 if e == '0' else 1
            arr[i] = r
            minv = min(minv, r)
            maxv = max(maxv, r)
        n = maxv - minv + 1
        tree = BITree(n)
        tree.update(0 - minv, 1)   # now always in [0, n-1]
        ans = 0
        for i, e in enumerate(arr):
            idx = e - minv
            ans += tree.query(idx-1)
            tree.update(idx, 1)
 
        return ans