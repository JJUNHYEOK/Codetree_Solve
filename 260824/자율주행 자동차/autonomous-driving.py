from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int,input().split())
x, y, d = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

visited[x][y] = True
cnt = 1 # 지나간 영역
turn_cnt = 0 # 회전 횟수

while True:
    d = (d+3)%4
    nx, ny = x+dx[d], y+dy[d]

    if graph[nx][ny] == 0 and not visited[nx][ny]:
        x, y = nx, ny
        visited[x][y] = True
        cnt += 1
        turn_cnt = 0
        continue


    turn_cnt += 1

    if turn_cnt == 4:
        bx, by = x - dx[d], y - dy[d]

        if graph[bx][by] == 1:
            break

        else:
            x, y = bx, by
            turn_cnt = 0

print(cnt)