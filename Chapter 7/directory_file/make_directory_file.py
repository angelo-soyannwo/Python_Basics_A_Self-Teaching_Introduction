
import os

def mk_dir_file(x, y):
	os.mkdir(x)
	os.chdir(x)
	file = open(y, "w")
	file.close()

def main():
	mk_dir_file("pwned", "file.txt")


if __name__ == "__main__":
	main()
