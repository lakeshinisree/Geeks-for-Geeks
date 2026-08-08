class Solution:
    def minEdgesReq(self, n, edges):
        lth=len(edges)
        if n-1>lth:
            return -1
        from collections import defaultdict
        adj=defaultdict(set)
        for sta,sto in edges:
            adj[sta].add(sto)
            adj[sto].add(sta)
        pr=[*range(n)]
        sz=[1]*n
        def find(x):
            a=x
            while x!=pr[x]:
                x=pr[x]
            pr[a]=x
            return x
        def union(x,y):
            x=find(x)
            y=find(y)
            if x==y:
                return False
            if sz[x]>sz[y]:
                x,y=y,x
            pr[x]=pr[y]
            sz[y]+=sz[x]
            return True
        for sta,sto in edges:
            union(sta,sto)
        st=set()
        for i in range(n):
            st.add(find(i))
        return len(st)-1