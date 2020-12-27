# n, m 공백으로 구분하여 입력 받기
n, m = map(int, input().split())

# 초기화
result = 0
for i in range(n):
    data = list(map(int, input().split()))
    # 입력 받은 수 중 가장 작은 수
    min_value = min(data)
    # 가장 작은 수 중에서 가장 큰 수
    result = max(result, min_value)

print(result)
