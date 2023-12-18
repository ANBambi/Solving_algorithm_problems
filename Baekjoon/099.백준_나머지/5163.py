# backjoon 5163번 

# 작성일자: 2023-10-06 , 작성자: 이민영

# 첫 번째 줄은 입력 데이터 세트의 K이고 다음으로 K개의 데이터 세트이며 각각의 형태는 다음과 같습니다:
# 첫 번째 줄은 정수 b와 부동 소수점 번호 w를 포함합니다. b ≥ 0은 Pooh가 사용하고 있는 풍선의 개수이고, w는 Pooh의 무게(그램)입니다.
# 그 다음에 b개의 선이 나타나며, 각각은 부동 소수점 숫자 ri ≥ 0을 포함합니다. 이것은 i번째 풍선의 반지름(cm)입니다.

# 각 데이터 집합에 대해 "데이터 집합 x:"를 한 줄에 출력하고, 여기서 x는 자신의 숫자입니다. 
# 다음 줄에는 풍선이 함께 푸를 들 수 있는지 여부에 따라 "예" 또는 "아니오"를 출력합니다. 각 데이터 집합 뒤에는 빈 줄이 이어야 합니다.

import math

T = int(input())
for i in range(1, T+1):
    b,w = map(float, input().split())
    
    balloon=[]
    for j in range(int(b)):
        balloon.append(float(input()))
    
    sb = []
    for r in balloon:
        sb.append(float(input()))
    
    sb = sum(sb)
    sb = sb / 1000
    
    if sb >= w:
        answer = "Yes"
    else:
        answer = "No"
        
    print(f"Data Set {i}:")
    print(answer)
    print()
              