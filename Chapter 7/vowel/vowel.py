import string


def clean(x):
	alphabet = string.ascii_lowercase + string.ascii_uppercase
	#find first letter character in the string
	for i in range(len(x)):
		if x[i] in alphabet:
			return x[i:]

def main():
	r = open("text.txt", "r")
	data = r.read().split()
	print(data, end="\n\n\n")
	data = list(set(map(clean, data)))

	vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
	vowel_words = [i for i in data if i[0] in vowels]
	print("The following words in the file begin with a vowel:")
	for i in vowel_words:
		print(i)	

if __name__ == "__main__":
	main()
