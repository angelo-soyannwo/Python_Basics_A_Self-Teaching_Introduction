
def make_withdraw(balance):
	def withdraw(amount):
		nonlocal balance
		if amount > balance:
			print('insufficient funds')
			return
		else:
			balance = balance - amount
		return balance
	return withdraw

def main():
	wd = make_withdraw(100)
	wd(20)
	wd(40)
	print(wd(30))
	wd(50)

if __name__ == '__main__':
	main()
