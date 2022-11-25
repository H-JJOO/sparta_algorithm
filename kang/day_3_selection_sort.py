input = [4, 6, 2, 9, 1]


def selection_sort(array):
    n = len(array) # 루프 카운트!
    for i in range(n - 1): # 이번에는 i ~ n - 2까지 돌면서 실험군을 선택해요!
        min_index = i # i번째에 들어갈 최소값을 찾아요! 파티션!
        for j in range(n - i): # j ~ n - 1까지 돌면서 대조군을 선택해요!
            # 현재 최소값으로 설정된 친구보다 더 작은 친구를 발견하면!
            if array[i + j] < array[min_index]: # i 는 출발지! j 는 n에서 i 를 뺀
                min_index = i + j # 최소값 인덱스를 갱신합니다!
        # 루프를 한 번 돌면 최소값 선정 1번이 끝난거에요!
        # 인덱스 i에 위치할 친구의 인덱스 min_index에 위치한 친구를 i 인덱스로 보내고
        # 원래 인덱스 i에 위치한 친구는 min_index 인덱스로 보냅니다! swap!
        array[i], array[min_index] = array[min_index], array[i]
    return array


selection_sort(input)
print(input)

print("정답 = [1, 2, 4, 6, 9] / 현재 풀이 값 = ",selection_sort([4, 6, 2, 9, 1]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",selection_sort([3,-1,17,9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",selection_sort([100,56,-3,32,44]))