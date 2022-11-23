input = "tamato"


#        01234
# 1. index 0 이랑 n-1 같으면 true
# 2. index 1 이랑 n-2 같으면 true

def is_palindrome(string):
    n = len(string)
    for i in range(n):
        if string[i] != string[n - 1 - i]:
            return False

    return True


print(is_palindrome(input))
