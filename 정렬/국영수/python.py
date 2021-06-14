n = int(input())

student = []

for _ in range(0,n):
    input_data = input().split()
    student.append((input_data[0],int(input_data[1]),int(input_data[2]),int(input_data[3])))

student_sorted = sorted(student, key = lambda x : (-x[1],x[2],-x[3],x[0]))

for x in student_sorted:
    print(x[0])