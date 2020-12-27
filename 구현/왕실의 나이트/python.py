location = input()
row = int(location[1])
# a를 좌표 1로 변경
col = int(ord(location[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방향 정의
dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [-1, -2, -2, -1, 1, 2, 2, 1]

# 8가지 방향에 대하여 이동가능한지 확인
result = 0
for i in range(0, 8):
    next_row = row + dx[i]
    next_col = col + dy[i]
    # 이동 가능할때 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_col >= 1 and next_col <= 8:
        result += 1

print(result)

# 나이트가 이동할 수 있는 8가지 방향 묶어서 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1),
         (2, 1), (1, 2), (-1, 2), (-2, 1)]
result2 = 0
for step in steps:
    next_row = row + step[0]
    next_col = col + step[1]
    if next_row >= 1 and next_row <= 8 and next_col >= 1 and next_col <= 8:
        result2 += 1

print(result2)
