
import os

def main():
	x = input("Please enter the name of:\t")
	a = input("Please enter new name of the file:\t")
	os.rename(x, a)
	print(os.getcwd())

if __name__ == "__main__":
	main()
