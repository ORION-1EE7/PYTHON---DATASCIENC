
import sys

def my_len(obj):
    count = 0
    for item in obj:
        count += 1
    return count

def str_to_int(s):
    result = 0
    sign = 1
    i = 0
    n = my_len(s)

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



try:
    ac = my_len(sys.argv)
    assert ac == 2, "more than one argument is provided"
    assert sys.argv[1].isnumeric, "argument is not an integer"
    num = str_to_int(sys.argv[1])
    # print(num)
    if num % 2 == 0:
        print("I'm even")
    elif num % 2 != 0:
        print("I'm odd")
except AssertionError as error:
    print(error)