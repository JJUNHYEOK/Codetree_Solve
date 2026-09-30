import sys
from collections import deque

input = sys.stdin.readline

N, K, L = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


# 축적
def add():
    new_maps_dust = [row[:] for row in maps]

    for i in range(N):
        for j in range(N):
            if maps[i][j] > 0:
                new_maps_dust[i][j] += 5

    return new_maps_dust


# 확산
def spread():
    new_maps = [row[:] for row in maps]

    for i in range(N):
        for j in range(N):

            if maps[i][j] == 0:
                amount = 0

                for d in range(4):
                    nr = i + dr[d]
                    nc = j + dc[d]

                    if 0 <= nr < N and 0 <= nc < N:
                        if maps[nr][nc] > 0:
                            amount += maps[nr][nc]

                new_maps[i][j] = amount // 10

    return new_maps


# 이동
def move(a, b, idx):
    q = deque()
    q.append((a, b, 0))

    visited = [[False] * N for _ in range(N)]
    visited[a][b] = True

    min_dis = -1
    cand = []

    while q:
        cr, cc, dis = q.popleft()

        if min_dis != -1 and dis > min_dis:
            break

        if maps[cr][cc] > 0:
            cand.append((cr, cc))
            min_dis = dis
            continue

        for d in range(4):
            nr = cr + dr[d]
            nc = cc + dc[d]

            if 0 <= nr < N and 0 <= nc < N:
                if not visited[nr][nc] and maps[nr][nc] != -1:
                    blocked = False

                    for k in range(K):
                        if k != idx:
                            if robot[k][0] == nr and robot[k][1] == nc:
                                blocked = True
                                break

                    if blocked:
                        continue

                    visited[nr][nc] = True
                    q.append((nr, nc, dis + 1))

    if cand:
        cand.sort()
        return cand[0]


# 청소
def cleaning(r, c):
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    best_dir = -1
    best_sum = -1

    for d in range(4):
        total = min(maps[r][c], 20)

        dirs = [(d - 1) % 4, d, (d + 1) % 4]

        for nd in dirs:
            nr = r + dr[nd]
            nc = c + dc[nd]

            if 0 <= nr < N and 0 <= nc < N:
                if maps[nr][nc] > 0:
                    total += min(maps[nr][nc], 20)

        if total > best_sum:
            best_sum = total
            best_dir = d

    if maps[r][c] > 0:
        maps[r][c] = max(0, maps[r][c] - 20)

    dirs = [(best_dir - 1) % 4, best_dir, (best_dir + 1) % 4]

    for nd in dirs:
        nr = r + dr[nd]
        nc = c + dc[nd]

        if 0 <= nr < N and 0 <= nc < N:
            if maps[nr][nc] > 0:
                maps[nr][nc] = max(0, maps[nr][nc] - 20)


robot = []

for _ in range(K):
    r, c = map(int, input().split())
    robot.append([r - 1, c - 1])


for _ in range(L):

    # 1. 이동
    for k in range(K):
        r, c = robot[k]

        target = move(r, c, k)

        if target:
            nr, nc = target
            robot[k] = [nr, nc]

    # 2. 청소
    for k in range(K):
        r, c = robot[k]
        cleaning(r, c)

    # 3. 축적
    maps = add()

    # 4. 확산
    maps = spread()

    ans = 0

    for i in range(N):
        for j in range(N):
            if maps[i][j] > 0:
                ans += maps[i][j]

    print(ans)