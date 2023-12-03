N, B = map(int, input().split())

alphabet_list = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num_list = list(range(36))
result = ''

while N >= B:
    idx = N%B
    alphabet_idx = num_list.index(idx)
    result += alphabet_list[alphabet_idx]
    
    N = N // B
    
alphabet_idx = num_list.index(N)
result += alphabet_list[alphabet_idx]    
    
print(result[::-1])
