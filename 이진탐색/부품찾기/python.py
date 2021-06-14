### 이진 탐색

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) / 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        # 중간점의 값보다 찾고자 하는 값이 클 경우 오른쪽 확인
        else:
            start = mid +1
    return None

# N 가게의 부품수
n = int(input())
# 가게에 있는 전체 부품 번호를 공백으로 구분하여 입력
array = list(map(int,input().split()))
array.sort() # 이진 탐색을 위한 정렬
# M 손님이 요청한 부품의 개수
m = int(input())
# 손님이 요청한 전체 부품 번호를 공백으로 구분하여 입력
x = list(map(int,input().split()))

# 손님이 확인 요청한 부품 번호를 하나씩 확인
for i in x:
    # 해당 부품이 존재하는지 확인
    result = binary_search(array, i, 0, n-1)
    if result != None:
        print('yes',end=' ')
    else:
        print('no',end=' ')

### 계수 정렬

# N 가게의 부품 개수
n = int(input())
# 가능한 부품 개수만큼 배열 생성
array = [0] * 1000001
# 가게에 있는 전체 부품 번호를 입력 받아서 기록
for i in input().split():
    array[int(i)] = 1

# M 손님이 확인 요청한 부품 개수
m = int(input())
# 손님이 확인 요청한 전체 부품 번호를 공백으로 구분하여 입력
x = list(map(int,input().split))

# 손님이 확인 요청한 부품 번호를 하나씩 확인
for i in x:
    # 해당 부품이 존재하는지 확인
    if array[i] == 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')

### 집합 자료형

# n 가게의 부품 개수
n = int(input())
# 가게에 있는 전체 부품 번호를 입력 받아 집합(set) 자료형에 기록
array = set(map(int,input().split()))

# m 손님이 확인 요청한 부품 개수
m = int(input())
# 손님이 확인 요청한 전체 부품 번호
x = list(map(int, input().split()))

# 손님이 확인 요청한 번호를 하나씩 확인
for i in x:
    # 해당 부품이 존재하는지 확인
    if i in array:
        print('yes', end=' ')
    else:
        print('no', end=' ')
