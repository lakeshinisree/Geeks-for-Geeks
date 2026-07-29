from collections import Counter
class Solution:
    def minSubsets(self, arr):
        
        f = Counter(arr)
        
        ans = 0
        for num in arr:
            if num - 1 in f:
                continue
            ans += 1
        
        return ans