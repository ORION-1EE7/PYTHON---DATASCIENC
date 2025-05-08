import sys
import string

def main():
      
		if len(sys.argv) != 2:
			print("invalid input")
			return 0

		StrInput = sys.argv[1]
		upper = 0
		lower = 0
		punctuation = 0
		digit = 0
		space = 0
		chars = 0
		for c in StrInput:
			if c.isupper():
				upper += 1
			elif c.islower():
				lower += 1
			elif c in string.punctuation:
				punctuation += 1
			elif c.isdigit():
				digit += 1
			elif c == ' ':
				space += 1
			chars += 1
		print(f"the text contains {chars} characters")
		print(f"{upper} upper letters")
		print(f"{lower} lower letters")
		print(f"{punctuation} Punctuation marks")
		print(f"{space} spaces")
		print(f"{digit} digits")

if __name__ == "__main__":
    main()
