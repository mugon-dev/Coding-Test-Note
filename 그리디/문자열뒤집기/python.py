data = list(map(int,input()))
count0 = 0
count1 = 0
if data[0]==0:
    count1 += 1
else:
    count0 += 1
# 두번째 원소부터 시작
for i in range(1,len(data)):
    # 0,1 연속된 숫자가 바뀔때
    if data[i-1] != data[i]:
        # 현재 0으로 연속된 숫자이면  1로 변경
        if data[i] == 0:
            count1 += 1
        # 현재 1로 연속된 숫자이면  0으로 변경
        else:
            count0 += 1
#0으로 변경한 횟수와 1로 변경한 횟수 비교해서 최솟값 출력
print(min(count0,count1))

