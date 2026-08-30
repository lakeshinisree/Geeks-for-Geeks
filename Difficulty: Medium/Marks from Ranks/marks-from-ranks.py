class Solution:
    def getMarks(self, l, r, rank):
        n = len(rank)
        order = sorted(range(n), key=lambda i: rank[i])
        i = count = 0
        for start, end in zip(l, r):
            size = end - start + 1
            while i < n and (offset := rank[order[i]] - count) <= size:
                rank[order[i]] = start + offset - 1
                i += 1
            if i == n:
                break
            count += size
        return rank
