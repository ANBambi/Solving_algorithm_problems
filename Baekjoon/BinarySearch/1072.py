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
