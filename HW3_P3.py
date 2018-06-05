# Homework 3: Problem 3
# Henry Rybolt

from numpy import *

VOWELS = ['a', 'e', 'i', 'o', 'u'];
word = raw_input('Please enter a word: ') 

# if the word starts with a vowel, then print word + "hay"
if word[0] in VOWELS:
	print(word + "hay")
# else print the word with its first letter moved to the back + "ay"
else:
	print(word[1:] + word[0] + "ay")                   
