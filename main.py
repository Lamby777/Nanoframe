# imports
from termcolor import colored
from random import choice
import replit

sub = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")

prefixes = [
	"YourMom",
	"Mon",
	"Di",
	"Tri",
	"Tetra",
	"Penta",
	"Hexa",
	"Hepta",
	"Octa",
]

metals = [
	{"name": "Lithium", "ve": 1},
	{"name": "Beryllium", "ve": 2}
]

nonmetals = [
	{"name":"Oxygen", "ve":6}
]

def makeBond():
	m = choice(metals)
	nm = choice(nonmetals) #

print(colored("Welcome to Nanoframe!\n" \
	"Press enter to make a bond.", "red")); input()
while True:
	replit.clear()
	print(makeBond())
	input()