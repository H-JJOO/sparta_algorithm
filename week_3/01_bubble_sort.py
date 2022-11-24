input = [4, 6, 2, 9, 1]

# 1번째 : [4, 6, 2, 9, 1]
#              → → → →  비교!
# 2번째 : [4, 2, 6, 1, 9]
#              → → → 비교!
# 3번째 : [2, 4, 1, 6, 9]
#              → → 비교!
# 4번째 : [2, 1, 4, 6, 9]
#              →  비교!

def bubble_sort(array):
    n = len(array)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j+1] = array[j+1], array[j]

    return


bubble_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!

print(sorted(input))