import heapq

# 생성 방법
mylist = [] # 리스트 생성
heapq.heappush(mylist, 1) # 리스트에 데이터를 넣을때 heappq를 이용해 저장

# 기본 함수
heappush(mylist, data) # data를 list(heap 자료구조) 형태로 저장
heappop(mylist) # list(heap 자료구조)에서 데이터 꺼내기
heapify(mylist) # 일반적인 list를 heap 자료구조로 변화

* heapq 는 기본적인 list 객체를 대상으로 원소 삽입, 삭제(꺼내기) 등의 제공 함수를 통해 우선순위 큐를 구현함