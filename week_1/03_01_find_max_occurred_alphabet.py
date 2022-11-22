input = "hello my name is sparta"


def find_max_occurred_alphabet(string):
    # 알파벳 배열
    alphabet_array = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                      "t", "u", "v", "x", "y", "z"]

    # 최대 반복 수
    max_occurrence = 0
    # 최대 반복한 인덱스
    max_alphabet = alphabet_array[0]

    for alphabet in alphabet_array:
        occurrence = 0
        for char in string:
            if char == alphabet:
                occurrence += 1

        if occurrence > max_occurrence:
            max_alphabet = alphabet
            max_occurrence = occurrence

    return max_alphabet




result = find_max_occurred_alphabet(input)
print(result)