# ex07/sos.py

import sys

NESTED_MORSE = {
    "A": ".- ", "B": "-... ", "C": "-.-. ", "D": "-.. ",
    "E": ". ", "F": "..-. ", "G": "--. ", "H": ".... ",
    "I": ".. ", "J": ".--- ", "K": "-.- ", "L": ".-.. ",
    "M": "-- ", "N": "-. ", "O": "--- ", "P": ".--. ",
    "Q": "--.- ", "R": ".-. ", "S": "... ", "T": "- ",
    "U": "..- ", "V": "...- ", "W": ".-- ", "X": "-..- ",
    "Y": "-.-- ", "Z": "--.. ",
    "0": "----- ", "1": ".---- ", "2": "..--- ", "3": "...-- ",
    "4": "....- ", "5": "..... ", "6": "-.... ", "7": "--... ",
    "8": "---.. ", "9": "----. ",
    " ": "/ "
}

def encode_morse(text):
	result = ""
	try:
		for char in text:
			upper = char.upper()
			assert upper in NESTED_MORSE, "Invalid character in input"
			result += NESTED_MORSE[upper]
		print(result)
	except AssertionError as error:
		print(f"AssertionError: {error}")
		return 1

def main():
	try:
		assert len(sys.argv) == 2, "Usage: python sos.py \"message\""
		if encode_morse(sys.argv[1]) == 1:
			return 1
	except AssertionError as error:
		print(f"AssertionError: {error}")
if __name__ == "__main__":
	main()