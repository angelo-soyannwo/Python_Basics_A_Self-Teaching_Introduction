import re
import os

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
	'printf'
	]
	return keywords



#******** Lexer  ********
def lex(characters, keywords=keywords(), delimiters=delimiters(), operators=operators()):

	def isWhiteSpace(word):
		return word in [' ', '\n', '\t'] 


	def isComment(line):
		pos = line.find('//')
		if pos == -1:
			return False
		else:
			former = line[:pos]
			for i in former:
				if not isWhiteSpace(i):
					return False
		return True


	#delimiter correction to format each line correctly
	def delimiter_correct(line):
		"""
		Takes in a line of code as a string and returns a list object containing the tokens in that line
		"""

		if isComment(line):
			return ["//"]

		tokens = line.split(' ')
		for delimiter in delimiters:
			for token in tokens:
				if token == delimiter:
					pass

				elif delimiter in token:
					position = token.find(delimiter)
					tokens.remove(token)
					token.replace(delimiter, " ")
					extra = token[:position]
					token = token[position+1:]
					tokens.append(delimiter)
					tokens.append(extra)
					tokens.append(token)
				else:
					pass
		for token in tokens:
			if ' ' in token:
				tokens.remove(token)
				token.split(' ')
				tokens += token
	#Removes tokens that are whitespace characters
		return [token for token in tokens if not isWhiteSpace(token)]


	#Basic check to check the type of each token
	def basic_check(token):
		"""
		Takes in a token and returns a string containing the token and it's description
		"""
		#regular expression checks
		variable_pattern = re.compile(r'[a-zA-Z_][a-zA-Z0-9_]')
		header_pattern = re.compile(r'\w[a-zA-Z]+[.]h')
		integer_pattern = re.compile(r'\d')
		float_pattern =	re.compile(r"[-+]?\d*\.\d+|\d+")

		if token in keywords:
			return token + ': Keyword'
		elif token in delimiters.keys():
			description = delimiters[token]
			if description == 'TAB' or 'NEWLINE':
				return description
			else:
				return token + ': ' + delimiters[token]
		elif token in operators.keys():
			return token + ': ' + operator[token]

		elif re.match(variable_pattern, token):
			return token + ": " + "Variable"
		elif re.search(header_pattern, token):
			return token + ": " + 'Header'
		elif re.match(integer_pattern, token):
			return token + ": " + 'Integer'
		elif re.match(float_pattern, token):
			return token + ": " + 'Float'
		elif token == '':
			return "NEWLINE"
		else:
			return "Unknown token"
	lines = characters.split("\n")
	n = len(lines)
	tokens = []
	result = []
	tokens += [delimiter_correct(line) for line in lines]
	for i in range(n):
		for token in tokens[i]:
			result += [('line ' + str(i) + ": " + basic_check(token))]
	print(tokens)
	return result

def tokenize(path):
	if not os.path.isfile(path):
		raise ValueError('\'' + path + '\' is not a file')
	else:
		with open(path) as file:
			program = file.read()
			return lex(program)

def main():
	t = tokenize('/Users/angelosoyannwo/H_BASHIN Pythom programs/Chapter 8/example.txt')	
	for token in t:
		print(token)
if __name__ == "__main__":
	main()
