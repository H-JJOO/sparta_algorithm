input = [3, 5, 6, 1, 2, 4]

def is_number_exist(number, array):
    for num in array: # array 의 길이만큼 연산이 실행
        if number == num: # 비교 연산 1회 실행
            return True

    return False # N * 1 = N 만큼


result = is_number_exist(3, input)

print(result)

# 기억할 것!
# 1. 입력값에 비례해서 얼마나 늘어날지 파악해보자 1 ? N ? N^2 ?
# 2. 공간복잡도 보다는 시간 복잡도를 더 줄이기 위해 고민하자.
# 3. 최악의 경우에 시간이 얼마나 소요될지(빅오 표기법)에 대해 고민하자.