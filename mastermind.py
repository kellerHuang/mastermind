#!/usr/bin/python

import sys
import re
import itertools
import copy
# simple code to solve a guessing game of mastermind without duplicates

# function that takes in the current possible solutions and finds the best guess
def bestGuess(res,allGuess):
	rHigh = 0
	hGuess = ""
	for guess in res:
		guessArr = list(guess)
		minRem = -1
		for m in range(1,4):
			for n in range(1,4):
				correct = m
				position = n
				removed = 0
				for i in res:
					cor = 0
					pos = 0
					for index,j in enumerate(i):
						if guessArr[index] == j:
							cor += 1
						elif j in guessArr:
							pos += 1
					if cor == correct and pos == position:
						pass
					else:
						# remove from res
						removed += 1
				if minRem == -1 or removed < minRem:
					minRem = removed 
		if minRem > rHigh:
			rHigh = minRem
			hGuess = guess
	print(rHigh)
	return hGuess






slots = 3
nums = 9

possible = []
possibleNum = 0
correct = 0
position = 0
print("Loaded")
print("Type predicates in the format: <guess> <result>")

res = list(itertools.permutations('123456789',3))
allGuess = list(itertools.permutations('123456789',3))
#for i in res:
#	print(i)

while(1):
	corChoice = []
	posChoice = []
	string = input("Enter next predicate:")
	fin = string.split()
	guess = fin[0]
	guessArr = list(guess)
	correct = int(fin[1][0])
	position = int(fin[1][1])
	if correct + position > nums:
		print("Input Error. Please retry.")
		continue
	# remove impossible combinations
	newRes = copy.deepcopy(res)
	for i in res:
		cor = 0
		pos = 0
		for index,j in enumerate(i):
			if guessArr[index] == j:
				cor += 1
			elif j in guessArr:
				pos += 1
		if cor == correct and pos == position:
			pass
		else:
			# remove from res
			newRes.remove(i)
	res = newRes
	print("\nSTILL POSSIBLE SOLUTIONS\n")
	for i in res:
		print(i)
	print(len(res), end = "")
	print(" possible solution(s) left\nBest next guess is: ",end="")
	print(bestGuess(res,allGuess))


