import sys

input = sys.stdin.readline

n, m = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(n)]

dr = [0, -1, -1, -1, 0, 1, 1, 1]
dc = [1, 1, 0, -1, -1, -1, 0, 1]

ddr = [-1,-1,1,1]
ddc = [-1,1,1,-1]

supplements = [
    (n-2, 0),
    (n-2, 1),
    (n-1, 0),
    (n-1, 1)
]

for _ in range(m):
    d, p = map(int,input().split())
    d -= 1

    moved = []

    for r, c in supplements:
        nr = (r+dr[d]*p)%n
        nc = (c+dc[d]*p)%n

        moved.append((nr, nc))

    for r, c in moved:
        maps[r][c] += 1

    for r, c in moved:
        cnt = 0

        for nd in range(4):
            nr = r + ddr[nd]
            nc = c + ddc[nd]

            if 0 <= nr < n and 0 <= nc < n:
                if maps[nr][nc] > 0:
                    cnt += 1

        maps[r][c] += cnt

    visited =[[False]*n for _ in range(n)]

    for r, c in moved:
        visited[r][c] = True

    new = []

    for i in range(n):
        for j in range(n):

            if visited[i][j]:
                continue

            if maps[i][j] >= 2:
                maps[i][j] -= 2
                new.append((i, j))

    supplements = new  

    ans = 0

    for i in range(n):
        for j in range(n):
            ans += maps[i][j]

print(ans)