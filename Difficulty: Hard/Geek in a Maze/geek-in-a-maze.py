from collections import deque

class Solution:
    def numberOfCells(self, r: int, c: int, u: int, d: int,
                      mat: list[list[int]]) -> int:

        n = len(mat)
        m = len(mat[0])

        # Starting cell is blocked.
        if mat[r][c] == '#':
            return 0

        INF = 10**18

        # dist[x][y] = minimum number of upward moves needed
        # to reach (x, y).
        dist = [[INF] * m for _ in range(n)]
        dist[r][c] = 0

        dq = deque([(r, c)])

        while dq:
            x, y = dq.popleft()
            cur = dist[x][y]

            # Four directions:
            # up    -> cost 1
            # down  -> cost 0
            # left  -> cost 0
            # right -> cost 0
            for dx, dy, cost in (
                (-1, 0, 1),
                (1, 0, 0),
                (0, -1, 0),
                (0, 1, 0)
            ):
                nx = x + dx
                ny = y + dy

                if not (0 <= nx < n and 0 <= ny < m):
                    continue

                if mat[nx][ny] == '#':
                    continue

                new_dist = cur + cost

                if new_dist < dist[nx][ny]:
                    dist[nx][ny] = new_dist

                    if cost == 0:
                        dq.appendleft((nx, ny))
                    else:
                        dq.append((nx, ny))

        ans = 0

        for x in range(n):
            for y in range(m):
                if mat[x][y] == '#':
                    continue

                if dist[x][y] == INF:
                    continue

                up_used = dist[x][y]

                # From:
                # down - up = x - r
                down_used = up_used + (x - r)

                if up_used <= u and down_used <= d:
                    ans += 1

        return ans