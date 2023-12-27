# 작성일자: 2023-12-22 FRI, 작성자: AN밤비
# 6236번 용돈관리
# 슈도코드

import sys


def isPossible(least, k, withdraws):
    """
    least : 현재까지 계산한 K번째 최소 금액
    K : 지출횟수
    withdraws : 일별 지출액 리스트
    """
    totalWithdraw = 0
    count = 1

    for withdraw in withdraws:
        # 현재 금액으로 지출
        totalWithdraw += withdraw
        if totalWithdraw > least:
            # 다음날로 넘어가기
            totalWithdraw = withdraw
            count += 1

    return count <= k


def binarySearch(start, end, k, withdraws):
    """
    start: 이분 탐색 시작값
    end: 이분 탐색 종료값
    k: 지출 횟수
    withdraws: 일별 지출액 리스트
    """
    result = 0

    while start <= end:
        mid = (start + end) // 2

        if isPossible(mid, k, withdraws):
            result = mid
            end = mid - 1
        else:
            start = mid + 1

    return result


def main():
    days, k = map(int, sys.stdin.readline().split())
    withdraws = [int(sys.stdin.readline()) for _ in range(days)]

    start = max(withdraws)
    end = sum(withdraws)

    result = binarySearch(start, end, k, withdraws)
    print(result)


if __name__ == "__main__":
    main()

# 함수 isPossible(least, k, withdraws):
#     totalWithdraw = 0
#     count = 1

#     반복문 withdraw in withdraws:
#         totalWithdraw += withdraw
#         만약 totalWithdraw > least이면:
#             totalWithdraw = withdraw
#             count += 1

#     count <= k 반환


# 함수 binarySearch(start, end, k, withdraws):
#     result = 0

#     while반복문 start <= end:
#         mid = (start + end) // 2

#         만약 isPossible(mid, k, withdraws)이면:
#             result = mid
#             end = mid - 1
#         아니면:
#             start = mid + 1

#     result 반환


# 함수 main():
#     days, k = stdin에서 읽은 값
#     withdraws = []

#     반복문 _ in range(days):
#         withdraw = stdin에서 읽은 값
#         withdraws에 withdraw 추가

#     start = withdraws 중 최댓값
#     end = withdraws의 합

#     result = binarySearch(start, end, k, withdraws)
#     result 출력
