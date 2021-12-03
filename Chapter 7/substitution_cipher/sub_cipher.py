
import string

#function to create a dictionary that contains the character offset the key value

def cipher(key):	
	characters = string.printable
	cipher = {}
	for i in characters:
		cipher[i] = {chr((ord(i) + key)%100)}
	return cipher
		
#remove curly braces and apostrophes from each character in cipher text "{'M'}" -> "M"

def clean(string):
	return string[2:-2]


def main():
	key = 4
# There are 100 printable characters

	code = cipher(key)
	file = open("text.txt", "r")
	r = file.read()
	file.close
	cipher_text = []

	for i in r:
		cipher_text += [str(code[i])]
	cipher_text = list(map(clean, cipher_text))

	coded_text = "".join(cipher_text) 
	print(cipher_text)
	print(coded_text)

	file2 = open("coded.txt", 'w')
	file2.write(coded_text)
	file2.close()

#	print([r])
#	print(len(r), end = "\n\n\n")
#	print([cipher_text])
#	print(len(cipher_text))
	

if __name__ == "__main__":
	main()
