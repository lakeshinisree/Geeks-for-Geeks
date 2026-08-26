class Solution:
    def isNegativeWeightCycle(self, V: int, edges: list[list[int]]) -> bool:
        # Initialize all vertices with distance 0
        dist = [0] * V
    
        # Relax all edges V times
        for i in range(V):
            updated = False
    
            for u, v, w in edges:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    updated = True
    
                    # If relaxation happens on the V-th iteration,
                    # a negative weight cycle exists.
                    if i == V - 1:
                        return True
    
            # No update means no negative cycle
            if not updated:
                break
    
        return False