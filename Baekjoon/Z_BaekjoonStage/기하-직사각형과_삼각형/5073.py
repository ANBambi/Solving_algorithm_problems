# 작성일자: 2024-04-17 TUE, 작성자: 이민영
# 백준 5073번 삼각형과 세 변


def triangle_length(length1, length2, length3):

    if max(length1, length2, length3) >= sum([length1, length2, length3]) - max(
        length1, length2, length3
    ):
        return "Invalid"
    elif length1 == length2 and length1 == length3:
        return "Equilateral"
    elif length1 == length2 or length2 == length3 or length1 == length3:
        return "Isosceles"
    else:
        return "Scalene"


while True:
    try:
        length1, length2, length3 = map(int, input().split())
        if length1 == 0 and length2 == 0 and length3 == 0:
            break
        print(triangle_length(length1, length2, length3))
    except ValueError:
        break
