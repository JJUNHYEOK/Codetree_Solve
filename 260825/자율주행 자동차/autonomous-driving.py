from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int,input().split())
r, c, d = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

cnt = 1
rotate_cnt = 0
visited[r][c] = True

while True:
    d = (d+3)%4

    nr, nc = r + dr[d], c + dc[d]

    if graph[nr][nc] == 0 and not visited[nr][nc]:
        r, c = nr, nc
        visited[nr][nc] = True
        cnt += 1
        rotate_cnt = 0
        continue

    rotate_cnt += 1

    if rotate_cnt == 4:
        br, bc = r - dr[d], c - dc[d]

        if graph[br][bc] == 1:
            break
        else:
            r, c = br, bc
            rotate_cnt = 0

print(cnt)