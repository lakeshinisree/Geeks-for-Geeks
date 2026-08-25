class Solution:

    def minMoves(self, arr):
    
        n = len(arr)
    
    
    
        pos = [0] * (n + 1)
    
    
    
        for i, x in enumerate(arr):
    
            pos[x] = i
    
    
    
        longest = 1
    
        current = 1
    
    
    
        for x in range(1, n):
    
            if pos[x] < pos[x + 1]:
    
                current += 1
    
            else:
    
                current = 1
    
    
    
            longest = max(longest, current)
    
    
    
        return n - longest