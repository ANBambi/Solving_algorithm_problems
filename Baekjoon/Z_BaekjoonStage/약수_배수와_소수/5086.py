# 작성일자 : 2023-12-28 THU, 작성자 : AN밤비
# 5086번 배수와 약수


while True:
    numberA, numberB = map(int, input().split())
    if numberA == 0 and numberB == 0:
        break

    if numberA <= numberB:
        if numberB % numberA == 0:
            print("factor")
        else:
            print("neither")
    elif numberA >= numberB:
        if numberA % numberB == 0:
            print("multiple")
        else:
            print("neither")
