input = [4, 6, 2, 9, 1]


def insertion_sort(array):
    n = len(array) # 루프 카운트!
    # 삽입 정렬의 0번째 인덱스는 정렬된 상태라고 판단하므로 인덱스가 1부터 시작해요!
    for i in range(1, n):
        # 현재 index 범위 내에서 비교를 시작하죠! 비교 방향은 끝에서부터 시작해요!
        for j in range(i):
            if array[i - j - 1] > array[i - j]: # 뒤의 값보다 앞의 값이 크면 바꿔줘요!
                array[i - j - 1], array[i - j] = array[i - j], array[i - j - 1]
            else: # 아니면 정렬된 상태이기 때문에 이번 루프는 바로 나가도 되어요!
                break
    return array

insertion_sort(input)
print(input)

print("정답 = [4, 5, 7, 7, 8] / 현재 풀이 값 = ",insertion_sort([5,8,4,7,7]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",insertion_sort([3,-1,17,9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",insertion_sort([100,56,-3,32,44]))