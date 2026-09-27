from collections import deque

N, r, c, d = map(int,input().split())
r -= 1
c -= 1
d -= 1

maps = [list(map(int,input().split())) for _ in range(N)]
visited = [[False]*N for _ in range(N)]

# N -> S -> W -> E
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

priority = [
    [0, 2, 3, 1],
    [1, 3, 2, 0],
    [2, 1, 0, 3],
    [3, 0, 1, 2]
]

visited[r][c] = True
ans = []
ans.append((r, c))
order = [2, 1, 3, 0]

while True:
    moved = False

    for nd in priority[d]:
        nr = r + dr[nd]
        nc = c + dc[nd]

        if 0 <= nr < N and 0 <= nc < N:
            if maps[nr][nc] == 0 and not visited[nr][nc]:
                r = nr
                c = nc
                d = nd
                visited[nr][nc] = True
                ans.append((r, c))
                moved = True
                break

    if moved:
        continue

    q = deque()
    q.append((r, c))
    bfs_v = [[False]*N for _ in range(N)]
    bfs_v[r][c] = True
    target = None

    while q:
        size = len(q)
        candi = []

        for _ in range(size):
            cr, cc = q.popleft()

            for nd in order:
                nr = cr + dr[nd]
                nc = cc + dc[nd]

                if 0 <= nr < N and 0 <= nc < N:
                    if maps[nr][nc] == 0 and not bfs_v[nr][nc]:
                        bfs_v[nr][nc] = True
                        q.append((nr, nc))

                        if not visited[nr][nc]:
                            candi.append((nr, nc, nd))

        if candi:
            candi.sort()
            target = candi[0]
            break

    if target is None:
        break


    r, c, d = target
    visited[r][c] = True
    ans.append((r, c))

for rr, cc in ans:
    print(rr+1, cc+1)