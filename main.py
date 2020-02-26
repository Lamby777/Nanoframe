# imports
from termcolor import colored
from random import choice
import replit

sub = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")

prefixes = [
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
	{"name": "lithium", "ve": 1},
	{"name": "beryllium", "ve": 2}
]

nonmetals = [
	{"name":"oxygen", "ve":6, "dn": "oxide"}
]

def makeBond():
	m = choice(metals)
	nm = choice(nonmetals)
	bondname = ["{}"+m["name"], "{}"+nm["dn"]]
	# Algorithm
	if m["ve"] > nm["ve"]:
		pass
	elif m["ve"] < nm["ve"]:
		pass
	else:
		pass
	return bondname

print(colored("Welcome to Nanoframe!\n" \
	"Press enter to make a bond.", "red")); input()
while True:
	replit.clear()
	print(makeBond())
	input()