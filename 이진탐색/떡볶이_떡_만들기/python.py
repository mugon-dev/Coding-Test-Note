

# n,m 공백 구분 입력 받기
n,m = map(int,input().split( ))
# 떡 배열 받기
array = list(map(int,input().split()))

# 이진 탐색 초기화
start = 0
end = max(array)

# 이진 탐색
while(start < end):
    # 자르고 남은 떡
    total = 0
    # 자르는 기준
    mid = (start + end) // 2
    # 자르고 남은 떡 합계
    for x in array:
        # 떡보다 적게 잘라야 떡이 남음
        if x > mid: # 
            total += x - mid
    # 남은떡 합계가 작으면 왼쪽 탐색
    if total < m:
        end = mid - 1
    # 남은떡 합계가 크면 오른쪽 탐색
    else:
        result = mid
        start = mid + 1

print(result)


