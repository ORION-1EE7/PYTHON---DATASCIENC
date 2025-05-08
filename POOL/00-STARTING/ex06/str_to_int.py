import my_len

def str_to_int(s):
    result = 0
    sign = 1
    i = 0
    n = my_len.my_len(s)

    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
              '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

    while i < n and s[i] == ' ':
        i += 1
    if i < n and (s[i] == '-' or s[i] == '+'):
        if s[i] == '-':
            sign = -1
        i += 1
    while i < n and s[i] in digits:
        result = result * 10 + digits[s[i]]
        i += 1
    while i < n:
        if s[i] != ' ':
            return None
        i += 1
    return result * sign