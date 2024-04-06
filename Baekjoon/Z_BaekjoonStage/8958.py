#
N = int(input())

score = []

for i in range(N):
    ox = input()
    for i in range(len(ox)):
        if (i == 0) & (ox[i] == "O"):
            score.append(1)
        elif (ox[i] == "O") & (ox[i - 1] != "O"):
            score.append(1)
        elif (ox[i] == "O") & (ox[i - 1] == "O"):
            score.append(score[i - 1] + 1)
        else:
            score.append(0)

    print(sum(score))
    score = []
