N, B = input().split()
B = int(B)
N = str(N)

result = int(N, B)
print(result)

# alphabet_list = list('0123456789ABCDEFGHOJKLMNOPQRSTUVWXYZ')
# num_list = list(range(36))

# sum = 0
# for i, char in enumerate(N):
#     num_idx = alphabet_list.index(char)
#     sum += (num_list[num_idx] * (B**(len(N)-1-i)))
    
# print(sum)