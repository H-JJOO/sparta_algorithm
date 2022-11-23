# 1. 최대값 찾기
# input = [3, 5, 6, 1, 2, 4, 10, 22, 1, 3, 44]
#
#
# def find_max_num(array):
#     # max_num = 0 이라고하나 배열의 첫번째 값을 넣든 결과는 같다. 취향차이
#     max_num = array[0]
#     for num in array:
#         if max_num < num:
#             max_num = num
#
#     return max_num
#
#
# print("현재 풀이 값 = ", find_max_num(input))
#
# # max_num = 0 변수를 할당하고 input 받을 array 의 배열의 인덱스만큼 반복문을 돌려서 max_num 보다 큰 숫자가 나오면 그 숫자를 max_num 에 대입한다.


# # 2. 1~100 텀퓨터가 고른 숫자 맞추기
# # import 외부의 페이지를 참조하기위한 키워드
# import random
#
# answer = random.randint(1, 100)
# count = 0 # 몇번만에 성공했는지 알려주기 위한 변수
# print('1~100 중 랜덤 숫자 하나를 정하였습니다. 과연 당신이 맞출 수 있을까요?!')
#list array
#
# while True: # 무한 루프
#     count += 1
#     guess = int(input('숫자 입력: ')) # 입력 받은 값을 숫자 값으로 치환
#     if guess > answer: # 사용자가 입력한 값보다 랜덤 숫자가 작으면 DOWN 출력!
#         print('DOWN')
#     elif guess < answer: # 사용자가 입력한 값보다 랜덤 숫자가 크면 UP 출력!
#         print('UP')
#     elif guess == answer: # 사용자가 입력한 값과 랜덤 숫자가 같으면 CORRECT 출력 후 종료
#         print('CORRECT')
#         break
#
# while True:
#
#
# print('숫자 입력한 횟수: %d번' % count)

# 1~100 중 선택하는 값이 select_num 일경우
# 1.while문 사용해서 입력값과 select_num 을 비교해서 비교값의 결과에따라 up down 을 출력해주고
# 2. select_num 과 입력값이 같으면 그 값을 출력하고 break

# 3. (연속된)문자열 요약하기

# def summarize_string(target_string):
#     n = len(target_string) # 순차적으로 탐색하기 위한 변수
#     count = 0
#     result_str = ''
#
#     # 0 ~ n-2까지 루프를 돌아요, 마지막 비교할 게 없기때문에
#     for i in range(n - 1):
#         # i번째 문자와 i + 1번째 문자가 같으면 count를 늘려야겠죠?!
#         if target_string[i] == target_string[i + 1]:
#             count += 1
#         else:
#             # i번째 문자와 i + 1번째 문자가 같지 않으면 카운트를 멈춰요!
#             # 그리고, 현재 문자랑 카운트를 혼합해서 요약표현을 만들어요!
#             # count 초기화는 잊지마세요!
#             result_str += target_string[i] + str(count + 1) + '/'
#             count = 0
#     # 위에서 n-1 까지 루프를 안 돌았던 이유는 n-1이 마지막 문자이기 때문에 결산을 하기 위함이에요!
#     result_str += target_string[n - 1] + str(count + 1)
#
#     return result_str
#
#
# input_str = "acccdeeeeffggzzzz"
#
# print(summarize_string(input_str))
