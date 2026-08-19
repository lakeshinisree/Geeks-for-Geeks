class Solution:
    def countTriplets(self, arr: list[int], l: int, r: int) -> int:
        n = len(arr)
        arr.sort()
    
        def at_most(max_sum: int) -> int:
            count = 0
    
            for i in range(n - 2):
                j = i + 1
                k = n - 1
    
                while j < k:
                    total = arr[i] + arr[j] + arr[k]
    
                    if total <= max_sum:
                    # Since array is sorted, all elements
                    # from j+1 to k will also work.
                        count += k - j
                        j += 1
                    else:
                        k -= 1
    
            return count
    
        return at_most(r) - at_most(l - 1)