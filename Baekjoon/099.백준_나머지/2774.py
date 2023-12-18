# backjoon 2774번 아름다운 수

# 함수 정의: 문자열에서 각 숫자의 등장 횟수를 계산하는 함수
def count_digits(s):
    arr = [0] * 10  # 0부터 9까지의 숫자의 등장 횟수를 저장할 리스트를 초기화합니다.
    for char in s:  # 입력받은 문자열을 한 글자씩 확인합니다.
        arr[int(char)] += 1  # 해당하는 숫자의 등장 횟수를 1 증가시킵니다.
    return len([x for x in arr if x >= 1])  # 등장 횟수가 1 이상인 숫자들의 개수를 반환합니다.

# 프로그램의 진입점
if __name__ == "__main__":
    num_cases = int(input())  # 테스트 케이스의 개수를 입력받습니다.
    
    for _ in range(num_cases):  # 테스트 케이스의 개수만큼 반복합니다.
        line = input()  # 열을 입력받습니다.
        result = count_digits(line)  # count_digits 함수를 호출하여 결과를 얻습니다.
        print(result)  # 결과를 출력합니다.