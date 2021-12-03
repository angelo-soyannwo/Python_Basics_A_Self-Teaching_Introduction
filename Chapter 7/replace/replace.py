
#open and read the text data as lines
file = open("text.txt", "r+")
r = file.readlines()
file.close()

#Pop \n from each string
def clean(x):
	for i in range(len(x)):
		x[i] = x[i].replace("\n", "")
clean(r)

def paste(data, x, val):
	data = data.replace(x, val)
	return data


for i in range(len(r)):
	r[i] = paste(r[i], "n", "a")



new_file = open("text.txt", "w")

for i in range(len(r)):
	new_file.write(r[i])
	

file.close()


