input = "소주만병만주소"


def is_palindrome(string):
    if len(string) <= 1:
        return True
    if string[0] != string[-1]:
        return False
    return is_palindrome(string[1: -1])


print(is_palindrome(input))

# 문제가 축소되는 특징이 보여야함
# 특정 구조가 반복되는 것 같은 양상을 보았으면
# 재귀함수 시도 생각
# 재귀함수를 쓸경우 반드시 탈출 조건 작성