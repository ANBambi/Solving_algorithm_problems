# 작성일자: 2024-04-17 WED, 작성자: 이민영
# 백준 10101번 삼각형과 세 변

length1, length2, length3 = map(int, input().split())


def triangle_length(length1, length2, length3):

    while length1 == 0 and length2 == 0 and length3 == 0:
        if max(length1, length2, length3) > sum(length1, length2, length3) - max(
            length1, length2, length3
        ):
            return "Invalid"
        elif length1 == length2 and length1 == length3 and length2 == length3:
            return "Equilateral"
        elif length1 == length2 or length2 == length3 or length1 == length3:
            return "Isosceles"
        elif length1 != length2 and length2 != length3 and length1 != length3:
            return "Scalene"


print(triangle_length(length1, length2, length3))
