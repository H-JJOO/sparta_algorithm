top_heights = [6, 9, 5, 7, 4]




def get_receiver_top_orders(heights):
    answer = [0] * len(heights) # [0,0,0,0,0]
    while heights: # heights 가 빈 상태가 아닐때
        height = heights.pop()
        # [6,9,5,7]
        for idx in range(len(heights) - 1, 0, -1):  # 시작, 끝, 증감
            if heights[idx] > height: # 레이저가 박힌다면
                answer[len(heights)] = idx + 1 # idx + 1 : 인덱스가 아닌 위치를 알려줘야함
                # 스택에서 하나를 뺀 다음에 그 하나의 인덱스를 알기위해서는 현재 나와있는 스택의 길이가 인덱스다...
                break

    return answer


print(get_receiver_top_orders(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!