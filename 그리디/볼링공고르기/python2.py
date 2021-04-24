n,m = map(int,input().split())
ball = list(map(int,input().split()))
result = 0
# 1부터 10까지의 무게
array = [0] * 11

# 무게별로 카운팅
for i in ball:
    array[i] += 1

# 경우의 수
for i in range(1,m+1):
    # a가 선택했던 볼링공 제거
    n -= array[i]
    result += array[i] * n

print(result)

