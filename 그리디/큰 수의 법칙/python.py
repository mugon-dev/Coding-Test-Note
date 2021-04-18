# 배열의 크기, 숫자가 더해지는 횟수, 최대 연속되는 횟수
n, m, k = map(int, input().split())

# 배열 입력받기
data = list(map(int, input().split()))
# 배열 정렬
data.sort()
# 가장큰수
first = data[n-1]
# 두번째로 큰 수
second = data[n-2]

# 반복되는 배열의 수
count = m/(k+1)
# 나머지
remainder = m % (k+1)
print("나머지: ", remainder)

# 반복되는 수의 합
result = count*((first*k)+second)
# 나머지 합
if(remainder != 0):
    result += remainder*first

# 결과
print(result)

