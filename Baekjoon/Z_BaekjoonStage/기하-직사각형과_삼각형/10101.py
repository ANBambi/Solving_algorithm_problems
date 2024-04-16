# 작성일자: 2024-04-16 TUE, 작성자: 이민영
# 백준 10101번 삼각형 외우기


def triangle_type(angle1, angle2, angle3):
    if angle1 + angle2 + angle3 != 180:
        return "Error"
    elif angle1 == 60 and angle2 == 60 and angle3 == 60:
        return "Equilateral"
    elif angle1 == angle2 or angle1 == angle3 or angle2 == angle3:
        return "Isosceles"
    else:
        return "Scalene"


angle1 = int(input())
angle2 = int(input())
angle3 = int(input())

print(triangle_type(angle1, angle2, angle3))
