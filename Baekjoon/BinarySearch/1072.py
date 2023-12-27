# 작성일자: 2023-12-27 WED, 작성자: AN밤비
# 1072번 게임
# 슈도코드

# 게임횟수 : X
# 이긴 게임 : Y (Z%)
# 승률 : Z

# X와 Y 가 주어졌을때, 최소 몇 번을 더 해야 Z가 변하는지 구하기

import sys


def winningRatio(gamesPlayed, gamesWon):
    """
    gamesPlayed : 플레이한 횟수
    gamesWon : 이긴 횟수
    """
    return (gamesWon * 100) // gamesPlayed if gamesPlayed != 0 else 0


def binarySearch(targetRatio, currentRatio, totalGames, wonGames):
    start, end = 1, sys.maxsize
    result = -1

    while start <= end:
        mid = (start + end) // 2

        newGamesPlayed = totalGames + mid
        newWonGames = wonGames + mid
        newRatio = winningRatio(newGamesPlayed, newWonGames)

        if newRatio > targetRatio:
            result = mid
            end = mid - 1
        else:
            start = mid + 1
    return result


def main():
    try:
        gameCount, winCount = map(int, sys.stdin.readline().split())
    except ValueError:
        return
    if gameCount == 0:
        print("-1")
        return

    currentRatio = winningRatio(gameCount, winCount)
    targetRatio = currentRatio

    result = binarySearch(targetRatio, currentRatio, gameCount, winCount)

    if result == -1:
        print("-1")

    else:
        print(result)


if __name__ == "__main__":
    main()

# 함수 winningRatio(플레이한횟수, 이긴횟수):
#     만약 플레이한횟수가 0이 아니라면:
#         반환 (이긴횟수 * 100) // 플레이한횟수
#     그렇지 않으면:
#         반환 0

# 함수 binarySearch(목표비율, 현재비율, 총게임횟수, 이긴게임횟수):
#     시작 = 1
#     끝 = 최대정수값
#     결과 = -1

#     동안 시작이 끝보다 작거나 같을 동안:
#         중간 = (시작 + 끝) // 2

#         새로운게임횟수 = 총게임횟수 + 중간
#         새로운이긴게임횟수 = 이긴게임횟수 + 중간
#         새로운비율 = 이긴비율계산(새로운게임횟수, 새로운이긴게임횟수)

#         만약 새로운비율이 목표비율보다 크다면:
#             결과 = 중간
#             끝 = 중간 - 1
#         그렇지 않으면:
#             시작 = 중간 + 1

#     반환 결과

# 함수 main():
#     시도:
#         게임횟수, 이긴횟수 = 맵(int, 입력().나누기())
#     예외 ValueError:
#         반환

#     만약 게임횟수가 0이라면:
#         출력("-1")
#         반환

#     현재비율 = 이긴비율계산(게임횟수, 이긴횟수)
#     목표비율 = 현재비율

#     결과 = binarySearch(목표비율, 현재비율, 게임횟수, 이긴횟수)

#     만약 결과가 -1이라면:
#         출력("-1")
#     그렇지 않으면:
#         출력(결과)

# 만약 __name__ == "__main__"이라면:
#     main()
