#! /utils/helper.py

def first_words(input, words):
	for i in range(0, len(input)):
		# Count spaces in the string.
		if input[i] == ' ':
			words -= 1
		if words == 0:
			# Return the slice up to this point.
			return input[0:i]
	return ""
