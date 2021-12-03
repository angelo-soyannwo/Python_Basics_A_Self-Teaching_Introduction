import keyword

#1
def rev(string):
	return string[::-1]

#2
def string_utf(string, form="utf8"):
	return string.encode(encoding=form, errors="strict")


#3
def sum_ascii(string):

#split string into words
#split words into characters
#use ord to find ascii values

	def split_all(string):
		"""Splits string into each individual character"""
		if len(string) <= 1:
			return string.split()
		else:
			return [string[0]] + split_all(string[1:])

	return sum(list(map(ord, split_all(string))), 0)



#4
def find_string(string, value):

	"""return slice idex of a substring within a string"""
#define a function to count the characters in the string
#slice string from the string from i to string_characters
#if slice == value return ([i:i+string_length] the index of where the word is)
#else increment i

	def count_chr(string):
		if string == string[0]:
			return 1
		else:
			return  count_chr(string[1:]) + 1

	n = count_chr(string)
	x = count_chr(value)
	result = []
	for i in range(n+1):
		if string[i:i+x] == value:
			result += [(i, i+x)]
	return result




#5
def token(string):
	token_dict = {}
	n = string.split()
	for i in range(len(n)):
		token_dict['token_'+str(i)] = n[i]
	return token_dict

	

#6
#take in a dictionary
#Check which dictionary tokens are in the keyword list
#return an array containing those tokens

def check_keywords(dict):

	def is_keyword(sub_string):
		if sub_string in keyword.kwlist:
			return keyword
		
	return	[dict[i] for i in dict if is_keyword(dict[i])]


#7
def ans(dict):
	"""
	takes a dictionary input
	take each dictoinary string and use isalphanum to check if it is an alpha numeric string
	returns number of alpha numeric strings in the dictionary
	"""
	result = 0
	for i in dict:
		if dict[i].isalnum():
			result += 1
	return result



#8
def aString(dict):
	"""
	takes a dictionary input
	take each dictoinary string and use isalphanum to check if it is an alpha numeric string
	returns number of alpha numeric strings in the dictionary
	"""
	result = 0
	for i in dict:
		if dict[i].isalpha():
			result += 1
	return result

#9
def ns(dict):
	"""
	takes a dictionary input
	take each dictoinary string and use isanum to check if it is an alpha numeric string
	returns number of alpha numeric strings in the dictionary
	"""
	result = 0
	for i in dict:
		if dict[i].isdecimal():
			result += 1
	return result

#10
def sub_cypher(string, k):
	"""
	takes in a string
	for each character in the string we apply tranform function to change the character to the character with k + its ascii value
	return the new string
	"""

	def transform(character):
		return chr(ord(character) + k)

	result = ""
	#count the characters in the string
	n = 0
	copy = string
	while len(copy) > 0:
		n += 1
		copy = copy[1:]

	result = ""
	for i in range(n):
		result += transform(string[i])
	return result


def rev(string, k):
	n = 0
	copy = string
	while len(copy) > 0:
		n += 1
		copy = copy[1:]

	result = ""
	for i in range(n):
		result += chr(ord(string[i]) - k)
	return result

def main():
	t = "abc"
	t = sub_cypher(t, 4)
	print(t)
	print(rev(t, 4))
	for i in t:
		print(ord(i), end =", ")
	print()
#	print(ord(']'))
#	print(ord('^'))
#	print(ord("_"))

if __name__ == "__main__":
	main()
