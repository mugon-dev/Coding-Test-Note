data = list(map(int,input()))
result = 0
for i in data:
    if i <= 1:
        result += i
    elif result == 0:
        result += i
    else:
        result *= i
print(result)


