class Solution:
    def maxDiffSubArrays(self, arr):
        # code here
        mn = sys.maxsize
        mx = -sys.maxsize
        mn_curr = 0
        mx_curr = 0
        pref_mn_arr = []
        pref_mx_arr = []
        for i in arr:
            mn_curr += i
            mx_curr += i
            mn = min(mn, mn_curr)
            mx = max(mx, mx_curr)
            pref_mn_arr.append(mn)
            pref_mx_arr.append(mx)
            if mn_curr > 0:
                mn_curr = 0
            if mx_curr < 0:
                mx_curr = 0
                
        mn = sys.maxsize
        mx = -sys.maxsize
        mn_curr = 0
        mx_curr = 0
        suff_mn_arr = []
        suff_mx_arr = []
        for i in arr[::-1]:
            mn_curr += i
            mx_curr += i
            mn = min(mn, mn_curr)
            mx = max(mx, mx_curr)
            suff_mn_arr.append(mn)
            suff_mx_arr.append(mx)
            if mn_curr > 0:
                mn_curr = 0
            if mx_curr < 0:
                mx_curr = 0
            
        suff_mn_arr = suff_mn_arr[::-1]
        suff_mx_arr = suff_mx_arr[::-1]
        
        res = -sys.maxsize
        for i in range(len(arr)-1):
            res = max(res, abs(pref_mx_arr[i] - suff_mn_arr[i+1]), abs(suff_mx_arr[i+1] - pref_mn_arr[i]))
        return res
