import sys
import re


#******** Keywords, delimiters and operators in c++ ********
def operators():
	operators = {
	"+": "PLUS",
	"-": "MINUS",
	"*": "MUL",
	"/": "DIV",
	"%": "MOD",
	"+=": "PLUSEQ",
	"-=": "MINUSEQ",
	"*=": "MULEQ",
	"/=": "DIVEQ",
	"++": "INC",
	"--": "DEC",
	"|": "OR",
	"&&": "AND",
	}
	return operators



def delimiters():
	delimiters = {
	"//": "comment",
	"\t": "TAB",
	"\n": "NEWLINE",
	"(": "LPAR",
	")": "RPAR",
	"[": "LBRACE",
	"]": "RBRACE",
	"{": "LCBRACE",
	"}": "RCBRACE",
	"=": "ASSIGN",
	":": "COLON",
	",": "COMMA",
	";": "SEMICOL",
	"<<": "OUT",
	">>": "IN",
	}
	return delimiters

def keywords():
	keywords = [
	"auto",
	"bool",
	"break",
	"case",
	"catch",
	"char",
	"word",
	"class",
	"const",
	"continue",
	"delete",
	"do",
	"double",
	"else",
	"enum",
	"false",
	"float",
	"for",
	"goto",
	"if",
	"#include",
	"int",
	"long",
	"namespace",
	"not",
	"or",
	"private",
	"protected",
	"public",
	"return",
	"short",
	"signed",
	"sizeof",
	"static",
	"struct",
	"switch",
	"true",
	"try",
	"unsigned",
	"void",
	"while",
	"printf"
	]
	return keywords

#******** Lexer  *******
def lex(characters):

	def basic_check(token, keywords=keywords(), operators=operators(), delimiters=delimiters()):
		"""
		Takes in a token as well as the c++ keywords, operators and delimeters.
		Checks to see if said token evaluates to a native data type, keywords, or header
		"""

		#creates the main regular expressions used in c++

		var_pattern = re.compile(r'\w[a-zA-Z0-9_]')
		header_pattern = re.compile(r'[<]\w[a-zA-Z0-9_] + [.]h[>]')
		digits_pattern = re.compile(r'\d')
		float_pattern = re.compile(r"[-+]?\d*\.\d+|\d+",) 

		#Checks if a token is a keyword, operator, or delimiter
		if token in keywords:
			return token + ": Keyword"
		elif token in operators.keys():
			return token + ": " + operators.keys[token]
		elif token in delimiters.keys():
			description = delimiters[token]
			if description == 'TAB' or description == 'NEWLINE':
				return description
			else:
				return token + ": "  + delimiters[token]

		#Checks if a token is one of a header file, integer, float, or variable
		elif re.match(header_pattern, token):
			return token + ': ' + " Header"	
		elif re.match(digits_pattern, token):
			return token + ': ' + " Int"
		elif re.match(float_pattern, token):
			return token + ': ' + " float"
		elif re.match(var_pattern, token):
			return token + ': ' + " variable"
		else:
			return 'NEWLINE'

	def isWhiteSpace(word):
		return word in ['', " ", "\t", "\n"]

	def delimiter_corrections(line, delimiters=delimiters()):
		"""
		Takes in a line of the source code and splits it up into tokens - taking delimiters as their own functions, and removing whitespace characters.
		Returns a list object that contains the tokens.
		"""
		tokens = line.split(" ")
		for delimiter in delimiters:
			for token in tokens:
				if token == delimiter:
					pass 
				elif delimiter in token:
					pos = token.find(delimiter)
					tokens.remove(token)
					token = token.replace(delimiter, " ")
					extra = token[:pos]
					token = token[pos+1:]
					tokens.append(delimiter)
					tokens.append(extra)
					tokens.append(token)
				else:
					pass
			
		for token in tokens:
			if ' ' in token:
				tokens.remove(token)
				token = token.split(' ')
				tokens += token
		return [t for t in tokens if not isWhiteSpace(t)]

	lines = characters.split("\n")
	n = len(lines)
	result = []
	tokens = [delimiter_corrections(line) for line in lines]
#	print(tokens)
	for line_number in range(n):
		for token in tokens[line_number]:
			result += [("line " + str(line_number) + " " + basic_check(token))]
	return result




def tokenize(path):
	"""Returns a list of (line_number, token + token_description)"""

	with open(path) as file:
		program = file. read()
	return	lex(program)
		
def main():
	t = tokenize("/Users/angelosoyannwo/H_BASHIN Pythom programs/Chapter 8/example.txt")
	for i in t:
		print(i)
if __name__ == "__main__":
	main()
