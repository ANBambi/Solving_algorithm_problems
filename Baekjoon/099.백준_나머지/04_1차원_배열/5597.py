A = []
for studentNumberList in range(30):
    A.append(studentNumberList + 1)

for Number in range(28):
    attendNumber = int(input())
    A.remove(attendNumber)

print(A[0])
print(A[1])
