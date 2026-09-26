from collections import deque

N, r, c, d = map(int, input().split())
maps = [[0] * (N + 1)]

for _ in range(N):
    row = list(map(int, input().split()))
    maps.append([0] + row)

visited = [[False] * (N + 1) for _ in range(N + 1)]

# 1: 위, 2: 아래, 3: 왼쪽, 4: 오른쪽
dr = [0, -1, 1, 0, 0]
dc = [0, 0, 0, -1, 1]

# 직진 -> 좌회전 -> 우회전 -> 뒤돌기
priority = [
    [],
    [1, 3, 4, 2],  # 위
    [2, 4, 3, 1],  # 아래
    [3, 2, 1, 4],  # 왼쪽
    [4, 1, 2, 3]   # 오른쪽
]

visited[r][c] = True

answer = []
answer.append((r, c))


while True:

    moved = False

    for nd in priority[d]:
        nr = r + dr[nd]
        nc = c + dc[nd]

        if 1 <= nr <= N and 1 <= nc <= N:
            if maps[nr][nc] == 0 and not visited[nr][nc]:

                r = nr
                c = nc
                d = nd

                visited[r][c] = True
                answer.append((r, c))

                moved = True
                break

    # 바로 옆 칸으로 이동했다면 다음 턴
    if moved:
        continue

    q = deque()
    q.append((r, c, 0))

    bfs_v = [[False] * (N + 1) for _ in range(N + 1)]
    bfs_v[r][c] = True

    min_dist = -1
    candidates = []

    while q:
        cr, cc, dist = q.popleft()

        if min_dist != -1 and dist > min_dist:
            break

        # 실제 고래가 아직 방문하지 않은 바다
        if not visited[cr][cc]:
            min_dist = dist
            candidates.append((cr, cc))

        # BFS에서는 이미 방문했던 바다도 지나갈 수 있음
        for nd in range(1, 5):
            nr = cr + dr[nd]
            nc = cc + dc[nd]

            if 1 <= nr <= N and 1 <= nc <= N:
                if maps[nr][nc] == 0 and not bfs_v[nr][nc]:

                    bfs_v[nr][nc] = True
                    q.append((nr, nc, dist + 1))


    if not candidates:
        break

    candidates.sort()
    tr, tc = candidates[0]

    dist_map = [[-1] * (N + 1) for _ in range(N + 1)]

    q = deque()
    q.append((tr, tc))

    dist_map[tr][tc] = 0

    while q:
        cr, cc = q.popleft()

        for nd in range(1, 5):
            nr = cr + dr[nd]
            nc = cc + dc[nd]

            if 1 <= nr <= N and 1 <= nc <= N:
                if maps[nr][nc] == 0 and dist_map[nr][nc] == -1:

                    dist_map[nr][nc] = dist_map[cr][cc] + 1
                    q.append((nr, nc))

    move_order = [3, 2, 4, 1]

    while r != tr or c != tc:

        for nd in move_order:
            nr = r + dr[nd]
            nc = c + dc[nd]

            if 1 <= nr <= N and 1 <= nc <= N:

                # 목적지까지 한 칸 가까워지는 방향
                if dist_map[nr][nc] == dist_map[r][c] - 1:

                    r = nr
                    c = nc
                    d = nd

                    # 새로운 바다라면 출력 순서에 추가
                    if not visited[r][c]:
                        answer.append((r, c))

                    visited[r][c] = True

                    break
                
for rr, cc in answer:
    print(rr, cc)