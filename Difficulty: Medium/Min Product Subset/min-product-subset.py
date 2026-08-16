class Solution:
    def minProd(self, arr):
        mxgl=arr[0]
        mngl=arr[0]
        for ix in range(1,len(arr)):
            n=arr[ix]
            mngl,mxgl=min(mngl,mngl*n,mxgl*n,n),max(mxgl,mxgl*n,mngl*n,n)
        return mngl