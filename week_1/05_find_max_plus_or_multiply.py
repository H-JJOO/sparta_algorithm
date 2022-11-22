input = [0, 3, 5, 6, 1, 2, 4]


def find_max_plus_or_multiply(array):
    max_sum = 0
    for num in array:
        if num <= 1 or max_sum <= 1:
            max_sum += num
        else:
            max_sum *= num

    return max_sum


result = find_max_plus_or_multiply(input)
print(result)


# 이 코드의 시간복잡도는 N 이다
