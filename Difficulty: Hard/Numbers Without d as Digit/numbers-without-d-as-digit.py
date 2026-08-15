class Solution:
    def countWithout(self, n: int, d: int) -> int:
        n = list(map(int, str(n)))
        k = len(n)
        res = 0
        for i, c in enumerate(n):
            if c == d:
                res += c * 9**(k -i -1) - 1
                break
            elif c < d:
                res += c * 9**(k -i -1)
            else:
                res += (c - 1) * 9**(k -i -1)

        if d == 0:
            res += (9**k - 1)//8 
        return res