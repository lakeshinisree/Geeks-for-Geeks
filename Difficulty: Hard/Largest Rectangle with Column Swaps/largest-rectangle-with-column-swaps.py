class Solution:
    def maxArea(self, mat: list[list[int]]) -> int:
        # code here
        m, n = len(mat), len(mat[0])
        for r in range(1, m):
            for c in range(n):
                if mat[r][c] != 0:
                    mat[r][c] += mat[r-1][c]
    
        ans = 0
        for r in mat:
            r.sort()
            for c in range(n):
                area = r[c] * (n-c)
                ans = max(ans, area)
        return ans