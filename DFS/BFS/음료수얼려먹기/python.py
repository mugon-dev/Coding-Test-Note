n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

def dfs(x,y):
    # 주어진 범위를 벗어날 때 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면 
    if graph[x][y] == 0:
        # 해당 노드 방문 처리 (얼음으로 만들기)
        graph[x][y] = 1
        # 상하좌우 재귀적 호출 (상하좌우로 뚫려있는 곳도 얼음으로 만들기)
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    # 모든 노드에 방문
    return False

# 아이스크림 개수
result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) === True:
            result += 1

print(result)

