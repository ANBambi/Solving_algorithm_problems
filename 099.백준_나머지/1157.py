# baekjoon 1157번 단어 공부
# 작성일자 : 2023-10-16 , 작성자 : AN밤비

word = input().upper()
abc = list(set(word))
# set 사용 : 중복방지, 입력받은 애들만 확인용

b = []

for i in abc:
    b.append(word.count(i))
    
if b.count(max(b)) != 1:
    print('?')
else:
    print(abc[b.index(max(b))])
    

