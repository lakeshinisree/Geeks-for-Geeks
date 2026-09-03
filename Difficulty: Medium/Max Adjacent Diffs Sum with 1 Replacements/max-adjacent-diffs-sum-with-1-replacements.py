class Solution:
    def maxDiffSum(self, arr):
        stayed = replaced = 0
        for i in range(1, len(arr)):
            prev, curr = arr[i - 1], arr[i]
            stayed, replaced = (
                max(stayed + abs(prev - curr), replaced + abs(1 - curr)),
                max(stayed + abs(prev - 1), replaced)
            )
        return max(stayed, replaced)