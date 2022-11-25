input = [4, 6, 2, 9, 1]


def bubble_sort(array):
    n = len(array)  # array의 길이를 n에 저장해요! 루프 카운트 변수로 쓰겠죠?
    for i in range(n):  # 이건 array를 순차적으로 돌겠다는 뜻이구요!
        # 이건 버블정렬 알고리즘의 특성처럼 1개씩 줄어들면서 반복하며 비교를 해요.
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:  # 앞의 원소가 뒤의 원소보다 크면 바꿔야겠죠?
                # 파이썬의 엄청난 장점! 코드 한 줄로 swap 기능을 사용해요!
                # 보통 swap(변수 a, b값을 서로 바꿈) 기능은 temp와 같은 임시변수를 쓰거나
                # XOR 연산을 이용해서 해요! 이거 진짜 엄청 편리한 기능이에요!
                array[j], array[j + 1] = array[j + 1], array[j]

    return array


bubble_sort(input)
print(input)

print("정답 = [1, 2, 4, 6, 9] / 현재 풀이 값 = ", bubble_sort([4, 6, 2, 9, 1]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ", bubble_sort([3, -1, 17, 9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ", bubble_sort([100, 56, -3, 32, 44]))