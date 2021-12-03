
celsius = [10, 5, 13, 23, 6]
fahrenheit = [i*1.8 +32 for i in celsius]

def is_prime(x):
	half = x+1 //2
	state = ""
	for i in range(2, half):
		if x%i == 0:
			state = "False"
			break
	if state == "False":
		return False
	if state != False:
		return True

primes = [i for i in range(100) if is_prime(i)]

modulos = [i for i in range(100) if i%5 == 1]

t = "sadbhfoiqbwqwvueofioani wqeurnasf hiasojamvnbayeiaowuh"
t_vowels = [i for i in t if i in ["a", "e", "i", "o", "u"]]

numbers = [1, 2, 3, 4, 5, 6]
fourth = [i**4 for i in numbers]


def magnitude(x):
	if x >= 0:
		return x
	else:
		return x*-1
data = [-10, 5, 8, -23, 90, -6]
magnitudes = [magnitude(i) for i in data]

print(magnitudes)

