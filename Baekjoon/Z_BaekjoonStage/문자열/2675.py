# 작성일자 : 2023-12-27 WED, 작성자 : AN밤비
# 2675번 문자열 반복

testCase = int(input())

for i in range(testCase):
    repeat, words = map(str, input().split())
    wordList = []
    for word in range(len(words)):
        wordList.append(words[word] * int(repeat))

    print("".join(wordList))
