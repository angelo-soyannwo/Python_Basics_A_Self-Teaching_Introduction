


def clean(string):
	string = string.replace("\n", "")
	return string

def binary_convert(string):
	t = bytearray(string, encoding ='utf-8')	
	result = "".join(format(x, 'b') for x in t)
	return result

def split_word(word):
	result  = [char for char in word]
	return result

def main():
	file = open("test.txt", "r")
	data = file.readlines()
	file.close()

	file2 = open("text.txt", "w")


	#split line into words
	for i in range(len(data)):
		data[i] = clean(data[i])
		data[i] = data[i].replace(" ", ",")
		data[i] = data[i].split(",")



	#within lines split words into individual charaters
	for i in range(len(data)):
		for j in range(len(data[i])):
			data[i][j] = split_word(data[i][j])
	print(data)

	#convert characters to binary
	for i in range(len(data)):
		for j in range(len(data[i])):
			for z in range(len(data[i][j])):
				data[i][j][z] = binary_convert(data[i][j][z])

	#format character to be 8 digits long if it is not
	for i in range(len(data)):
		for j in range(len(data[i])):
			for z in range(len(data[i][j])):
				if len(data[i][j][z]) < 8:
					x = 8 - len(data[i][j][z])
					u = '0' * x
					data[i][j][z] = u + data[i][j][z]

	#concatenate characters into words
	for i in range(len(data)):
		for j in range(len(data[i])):
			word = ""
			for z in range(len(data[i][j])):
				word += data[i][j][z]
			data[i][j] = word
	
	#concatenate words into lines
	for i in range(len(data)):
		line = ""
		for j in range(len(data[i])):
			line += data[i][j]
			if j == len(data[i]) - 1:
#Use os.linsep() instead of line+= "binary for \n"
				line += "00001010"
				break
			line += "00100000"
		data[i] = line
	
	print(data)

	for i in range(len(data)):
		file2.write(data[i])
	file.close()
	file2.close()

###	print(len(data[0])%8)
	file2.close()
###	print(binary_convert(" ")) = 100000

	


if __name__ == "__main__":
	main()
