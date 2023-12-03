
dic = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

word = input()
# alphabets = []

for i in dic:
    # i 를 #로 대체하고 그 단어 길이 세기
    word = word.replace(i, "#")
    
print(len(word))

# N = input()
# result = len(N)
# for i in range(result):
#     if N[i] == "=" and not i == 0:
#         if N[i-1] == "c" or N[i-1] == "s":
#             result -= 1
#         if N[i-1] == "z" and N[i-2] == "d":
#             result -= 1
#         if N[i-1] == "z":
#             result -= 1
#     if N[i] == "-" and not i == 0:
#         if N[i-1] == "c" or N[i-1] == "d":
#             result -= 1
#     if N[i] == "j" and not i == 0:
#         if N[i-1] == "l" or N[i-1] == "n":
#             result -= 1

# print(result)