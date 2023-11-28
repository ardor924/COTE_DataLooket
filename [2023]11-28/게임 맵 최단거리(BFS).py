from collections import deque

# 문제풀이
def solution(maps):
    n, m = len(maps), len(maps[0])

    # 시작 지점과 방문 여부를 저장하는 2차원 배열
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True

    # 시작 지점을 큐에 저장
    queue = deque([(0, 0)])

    # 탐색
    while queue:
        x, y = queue.popleft()

        # 도착한 경우
        if x == n - 1 and y == m - 1:
            return visited[x][y]

        # 탐색 가능한 경우
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))

    # 도착할 수 없는 경우
    return -1



# 예시
maps1 = [
            [1, 0, 1, 1, 1], 
            [1, 0, 1, 0, 1], 
            [1, 0, 1, 1, 1], 
            [1, 1, 1, 0, 1], 
            [0, 0, 0, 0, 1]
        ]

maps2 = [
            [1, 0, 1, 1, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 1, 1, 1],
            [1, 1, 1, 0, 0],
            [0, 0, 0, 0, 1]
        ]

maps3 = [
            [1, 1, 1, 1, 0],
            [0, 0, 0, 1, 0],
            [0, 0, 1, 1, 0],
            [0, 0, 0, 1, 0],
            [0, 0, 0, 1, 1]
        ]


# 메인함수실행
if __name__ == "__main__":
    res1 = solution(maps1)
    res2 = solution(maps2)
    res3 = solution(maps3)
    print('res1:',res1)
    print('res2:',res2)
    print('res3:',res3)

    