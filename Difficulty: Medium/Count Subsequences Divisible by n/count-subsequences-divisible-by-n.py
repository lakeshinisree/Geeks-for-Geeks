class Solution:
    def countSubsequences(self, s: str, n: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * n

        for char in s:
            d = int(char)
            next_dp = list(dp)

            # Start a new subsequence containing just this digit
            next_dp[d % n] = (next_dp[d % n] + 1) % MOD

            # Append this digit to all previous remainders
            for rem in range(n):
                if dp[rem] > 0:
                    new_rem = (rem * 10 + d) % n
                    next_dp[new_rem] = (next_dp[new_rem] + dp[rem]) % MOD

            dp = next_dp

        return dp[0]