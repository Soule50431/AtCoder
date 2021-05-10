s = input()
len_s = len(s)


def is_palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False


if is_palindrome(s) \
        and is_palindrome(s[:int((len_s-1)/2)]) \
        and is_palindrome(s[int((len_s+3)/2)-1:]):
    print("Yes")
else:
    print("No")