input = [4, 6, 2, 9, 1]


def selection_sort(array):
    n = len(array)

    for i in range(n - 1):  # 맨 마지막에 하나 남은 원소 비교 안하니까
        min_index = i
        for j in range(n - i):  # 하나씩 줄어가는 구조
            if array[i + j] < array[min_index]:
                min_index = i + j # i + j = 현재 시도해 보고 있는 인덱스
        array[i], array[min_index] = array[min_index], array[i]
    return


selection_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!