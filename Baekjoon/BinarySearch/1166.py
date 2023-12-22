# 작성일자: 2023-12-22 FRI, 작성자: AN밤비
# 1166번 선물
# 슈도코드

# 함수 isPossible(중간, 길이, 갯수):
#     mid 길이로 만들 수 있는 선물의 수가 주어진 개수보다 크거나 같은지 확인

# 함수 binarySearch(길이, 박스갯수):
#     시작점, 끝점 = 1, length

#     결과 = 0
#     while 시작점 <= 끝점:
#         mid = (시작점 + 끝점) // 2

#         if isPossible(중간, 길이, 갯수):
#             결과 = mid
#             시작점 = mid + 1
#         else:
#             끝점 = mid - 1

#     결과 반환

# 함수 main():
#     length, Count(박스갯수)

#     결과 = binarySearch(길이, 박스갯수)
#     결과 출력

# main 함수 실행

n, l, w, h = map(int, input().split())

start = 0
end = max(l, w, h)
result = 0

for _ in range(100000):
    mid = (start + end) / 2

    cnt = (l // mid) * (w // mid) * (h // mid)

    if cnt >= n:
        result = mid
        start = mid
    else:
        end = mid
print("%0.10f" % result)
