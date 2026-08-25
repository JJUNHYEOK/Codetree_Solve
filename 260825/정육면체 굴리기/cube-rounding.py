import sys

input = sys.stdin.readline

n, m, x, y, k = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(n)]
cmd = list(map(int,input().split()))

dr = [0, 0, -1, 1] # E -> W -> N -> S
dc = [1, -1, 0, 0]
cube = [0, 0, 0, 0, 0, 0] # 6면 초기화(Top -> E -> W -> N -> S -> Bottom)

def rotate(dir):
    top, east, west, north, south, bottom = cube

    if dir == 1: # East
        cube[0], cube[1], cube[2], cube[5] = west, top, bottom, east

    if dir == 2: # West
        cube[0], cube[1], cube[2], cube[5] = east, bottom, top, west

    if dir == 3: # North
        cube[0], cube[3], cube[4], cube[5] = south, top, bottom, north

    if dir == 4: # South
        cube[0], cube[3], cube[4], cube[5] = north, bottom, top, south


for dir in cmd:
    d = dir
    nx, ny = x+dr[d-1], y+dc[d-1]

    if 0 <= nx < n and 0 <= ny < m:
        x, y = nx, ny
        rotate(d)
        if grid[nx][ny] == 0:
            grid[nx][ny] = cube[5]

        else:
            cube[5] = grid[nx][ny]
            grid[nx][ny] = 0

        print(cube[0])