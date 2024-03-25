# Selection Sort - 선택정렬 🐿️💚

<img src="https://velog.velcdn.com/images/yun8565/post/1bdd4fa7-4b57-46bd-b2a3-0afe29d10b9f/image.gif" alt="Alt text" height=250>

### 연습 문제

- 소트인사이드 : https://www.acmicpc.net/problem/1427

<br>

## 1. 시간 복잡도

- 선택 정렬의 시간 복잡도는 O(N²) 이다.

</br>

`※ 핵심 이론`

    최솟값 또는 최댓값을 찾고, 남은 정렬 부분의 가장 앞에 있는 데이터와 swap 하기

## 2. 선택 정렬 과정

</br>

    1. 남은 정렬 부분에서 최솟값 또는 최댓값을 찾는다.

    2. 남은 정렬 부분에서 가장 앞에 있는 데이터와 선택된 데이터를 swap한다.

    3. 가장 앞에 있는 데이터의 위치를 변경해(index++) 남은 정렬 부분의 범위를 축소한다.

    4. 전체 데이터 크기만큼 index가 커질 때까지, 즉 남은 정렬 부분이 없을때까지 반복한다.

## 3. 내림차순 선택정렬 예시 코드

    # 슈도 코드

    A(자릿수별로 구분해 저장한 리스트)
    A 리스트 저장

    for i 를 A 리스트만큼 반복:
        for j 를 i+1 ~ A 리스트 길이만큼 반복:
            현재 범위에서 Max 값 찾기
        현재 i의 값과 Max 값 중 Max 값이 더 크면 swap 수행

    A 리스트 출력

<br>

    # 구현 코드
    import sys
    print = sys.stdout.write
    A = list(input())

    for i in range(len(A)):
        Max = i
        for i in range(i+1, len(A)):
            if A[j] > A[Max]:
                Max = j
        if A[i] < A[Max]:
            temp = A[i]
            A[i] = A[Max]
            A[Max] = temp

    for i in range(len(A)):
        print(A[i])
