n = int(input())
x = list(map(int,input().split()))
x.sort()
group = 0
start = 0
for i in x:
    group += 1
    print(group)
    if group >= i:
    group = 0
    start += 1
print(start)

$