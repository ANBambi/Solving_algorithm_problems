# 작성일자: 2024-06-10 MON, 작성자: 이민영
# 백준 1018번 체스판 다시 칠하기


def count_mismatches(board, start_row, start_col, first_color):
    count = 0
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                if board[start_row + i][start_col + j] != first_color:
                    count += 1
            else:
                if board[start_row + i][start_col + j] == first_color:
                    count += 1

    return count


N, M = map(int, input().split())
chess_board = [input().strip() for _ in range(N)]

min_mismatches = float("inf")

for i in range(N - 7):
    for j in range(M - 7):
        mismatches_B = count_mismatches(chess_board, i, j, "B")
        mismatches_W = count_mismatches(chess_board, i, j, "W")
        min_mismatches = min(min_mismatches, mismatches_B, mismatches_W)

print(min_mismatches)
