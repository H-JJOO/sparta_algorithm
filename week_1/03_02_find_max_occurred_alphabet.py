input = "hello my name is sparta"


def find_max_occurred_alphabet(string):
    # 알파벳 26개 배열 생성
    alphabet_occurrence_array = [0] * 26


    # 배열의 index 만큼 반복
    for char in string:
        # 해당 문자가 알파벳이 아닌가? 아니면 continue
        if not char.isalpha():
            continue #(아래 코드를 건너뛴다)
        # 알파벳 26개 인덱스
        arr_index = ord(char) - ord('a')
        # 해당 인덱스 알파벳 1 증가
        alphabet_occurrence_array[arr_index] += 1

    # 최대 빈도수 알파벳
    max_occurrence = 0
    # 최대 빈도수 알파벳 인덱스
    max_alphabet_index = 0
    # range(len(alphabet_occurrence_array) == range(26)
    for index in range(len(alphabet_occurrence_array)):
        # index 0 -> alphabet_occurrence 3
        # 알파벳 별 빈도수
        alphabet_occurrence = alphabet_occurrence_array[index]

        # 알파벳 빈도수가 가장 큰 녀석이라고 판단되었기 때문에
        if alphabet_occurrence > max_occurrence:
            # 알파벳 인덱스 업데이트
            max_alphabet_index = index
            # 알파벳 빈도수 업데이트
            max_occurrence = alphabet_occurrence

    # max_alphabet_index + ord('a') == 0, 최대빈도수 알파벳은 0번째 인덱스, 즉 말파벳 a
    # 인덱스 0 dmf dnlgo ord('a') 즉 아스키코드 97 을 빼줬기 때문에 다시 더해줘서 아스키 코드 복귀
    # 결국 0 + 97 = 97 아스키코드인 a 출력
    result = chr(max_alphabet_index + ord('a'))

    return result


result = find_max_occurred_alphabet(input)
print(result)
