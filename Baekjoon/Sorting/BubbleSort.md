# Bubble Sort - 버블정렬 🐿️💚

<img src="https://www.learnsimpli.com/wp-content/uploads/2021/05/How-bubble-sort.gif" alt="Alt text" height=250>

### 연습 문제

- 수 정렬하기 : https://www.acmicpc.net/problem/2750

<br>

## 1. 시간 복잡도

- 버블 정렬의 시간 복잡도는 O(N²) 이다.
- N의 최대 범위가 1,000 일 경우 가능

</br>

`※ 핵심 이론`

    두 인접한 데이터의 크기를 비교해 정렬하는 방법
    루프(loop)를 돌면서 인접한 데이터 간의 swap 연산으로 정렬

## 2. 버블 정렬 과정

</br>

    1. 비교 연산이 필요한 루프 범위를 설정한다.

    2. 인접한 데이터 값을 비교한다.

    3. swap 조건에 부합하면 swap 연산을 수행한다.

    4. 루프 범위가 끝날 때까지 2. ~ 3. 을 반복한다.

    5. 정렬 영역을 설정한다. 다음 루프를 실행할 때는 이 영역을 제외한다.

    6. 비교 대상이 없을 때까지 1. ~ 5. 를 반복한다.

`만약, 특정한 루프의 전체 영역에서 swap이 한 번도 발생하지 않았다면 그 영역 뒤에 있는 데이터가 모두 정렬됐다는 뜻이므로 프로세스를 종료해도 됨`

## 3. 예시 코드

    # 슈도 코드

    N(정렬할 수 개수)
    A(수 저장 리스트 선언 및 입력 데이터 저장)

    for i를 0 ~ N-1 만큼 반복:
        for j를 0 ~ N-1-i 만큼 반복:
            현재 A리스트의 값보다 1칸 오른쪽 리스트의 값이 더 작으면 두 수 바꾸기

    A 리스트 출력

<br>

    # 구현 코드

    N = int(input())
    A = [0] * N

    for i in range(N-1):
        for j in range(N-1-i):
            if A[j] > A[j+1]:
                temp = A[j]
                A[j] = A[j+1]
                A[j+1] = temp

    for i in rang(N):
        print(A[i])
