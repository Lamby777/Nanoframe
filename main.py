# imports
from termcolor import colored
from random import choice
import replit

sub = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")

metals = [
	{"name": "Lithium", "ch": 1}
]

nonmetals = [
	#
]

print(colored("Welcome to Nanoframe!\n" \
			"Press enter to make a bond.", "red")); input()
while True:
	replit.clear()
	print()
	input()