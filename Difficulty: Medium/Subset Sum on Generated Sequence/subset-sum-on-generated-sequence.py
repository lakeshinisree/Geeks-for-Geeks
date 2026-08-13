class Solution:
    def isPossible(self, arr, s, x):
        nums = [s]
        total = s

        for a in arr:
            nxt = total + a

            if nxt > x:
                break

            nums.append(nxt)
            total += nxt

        # Greedily take the largest possible number
        for num in reversed(nums):
            if num <= x:
                x -= num

            if x == 0:
                return True

        return False