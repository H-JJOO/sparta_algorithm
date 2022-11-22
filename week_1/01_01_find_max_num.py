input = [3, 5, 6, 1, 2, 4]


def find_max_num(array):
    # 배열 인덱스 만큼 반복
    for num in array:
        for compare_num in array:
            # 비교숫자보다 작으면 break
            if num < compare_num:
                break
            else:
                return num


print("정답 = 6 / 현재 풀이 값 = ", find_max_num([3, 5, 6, 1, 2, 4]))
print("정답 = 6 / 현재 풀이 값 = ", find_max_num([6, 6, 6]))
print("정답 = 1888 / 현재 풀이 값 = ", find_max_num([6, 9, 2, 7, 1888]))
