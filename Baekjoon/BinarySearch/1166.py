# 작성일자: 2023-12-22 FRI, 작성자: AN밤비
# 1166번 선물
# 슈도코드

# 입력으로 큐브의 개수 n과 각 큐브의 길이 l, w, h를 받음
# 이분 탐색을 위한 시작점 start를 0으로, 끝점 end를 max(l, w, h)로 초기화
# 결과를 저장할 변수 result를 0으로 초기화
# 100,000번 반복
#    현재 범위의 중간값을 계산하여 변수 mid에 저장
#    mid를 이용하여 큐브의 개수 cnt를 계산
#    cnt가 목표 개수 n 이상이면 결과 result를 mid로 업데이트하고 범위를 오른쪽으로 좁힘 (start = mid)
#    cnt가 목표 개수 n 미만이면 범위를 왼쪽으로 좁힘 (end = mid)
# 최종 결과 result를 소수점 10자리까지 출력

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
