
def revert(array):
	u = ""
	for i in range(len(array)):
		s= array[i]
		for j in range(0, len(s), 8):
			u += chr(int(s[j:j+8],2))
	return u

def s2b(string):
	return chr(int(string, 2))

def binary_convert(string):
        t = bytearray(string, encoding ='utf-8')
        result = "".join(format(x, 'b') for x in t)
        return result

def main():
	r = open("text.txt", "rb+")
	data = r.readlines()
	r.close()
	file2 = open("text2.txt", "w+")

	t = revert(data)
	file2.write(t)
	file2.close()	

if __name__ == "__main__":
	main()
