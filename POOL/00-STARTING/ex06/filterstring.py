import sys
import str_to_int
import ft_filter 
import my_len

def main():
    try:
        ac = my_len.my_len(sys.argv)
        assert ac == 3, "Exactly two arguments required: a string and an integer."
        n = str_to_int.str_to_int(sys.argv[2])
        assert n == None, "the arguments are bad"
        words = sys.argv[1].split()
        filtered = ft_filter(lambda item: my_len.my_len(item) > n, words)
        result = []
        for word in filtered:
            result.append(word)
        print(result)
    except AssertionError as error:
        print(f"AssertionError: {error}")

if __name__ == "__main__":
    main()
