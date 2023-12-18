N = int(input())
num_list = []

num = 0
num_count = 0

while num_count < N:
    num += 1
    num_count += num

num_count -= num

if num % 2 == 0:
    i = N - num_count
    j = num - i + 1
else:
    i = num - (N - num_count) + 1
    j = N - num_count

print(f"{i}/{j}")