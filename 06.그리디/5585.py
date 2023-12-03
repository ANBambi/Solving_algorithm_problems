n = 1000 - int(input())

# 동전 종류 저장 리스트 선언
currency = [500, 100, 50, 10, 5, 1]
# 동전 갯수 저장할 변수
count = 0
# 동전의 가치 리스트의 인덱스 변수
i = 0

while n != 0:
    # 동전의 개수를 저장
    count += n // currency[i]
    # 동전의 가치로 나눈 나머지를 저장
    n %= currency[i]
    # 인덱스 1 증가 ; 뒤로 넘어가기
    i += 1

print(count)
