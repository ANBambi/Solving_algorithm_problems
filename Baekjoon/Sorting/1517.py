import sys

input = sys.stdin.readline

result = 0


def mergeSort(start, end):
    global result
    if end - start < 1:
        return
    middle = int(start + (end - start) / 2)
    mergeSort(start, middle)
    mergeSort(middle + 1, end)
    for i in range(start, end + 1):
        tmp[i] = A[i]
    k = start
    index1 = start
    index2 = middle + 1
    while index1 <= middle and index2 <= end:
        if tmp[index1] > tmp[index2]:
            A[k] = tmp[index2]
            result = result + index2 - k
            k += 1
            index2 += 1
        else:
            A[k] = tmp[index1]
            k += 1
            index1 += 1
    while index1 <= middle:
        A[k] = tmp[index1]
        k += 1
        index1 += 1
    while index2 <= end:
        A[k] = tmp[index2]
        k += 1
        index2 += 1


N = int(input())
A = list(map(int, input().split()))
A.insert(0, 0)
tmp = [0] * int(N + 1)
mergeSort(1, N)
print(result)
