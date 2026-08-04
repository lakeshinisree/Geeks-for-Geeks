class Solution:
    def countPairs(self, arr: list[int], k: int) -> int:
        import bisect
        arr.sort()
        ret=sto=0
        for sta,ve in enumerate(arr):
            sto=bisect.bisect_left(arr,ve+k,sto)
            ret+=sto-sta-1
        return ret

