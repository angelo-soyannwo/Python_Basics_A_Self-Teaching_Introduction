


def numdict():
	numberDict = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', \
6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', \
11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty', 50: 'Fifty', 60: 'Sixty', 70:'Seventy', 80: 'Eighty', 90: 'Ninety', 100: 'hundred', 1000:'oneThousand'}	
	return numberDict


def n2w(num, dict):
	result = ''
	if num == 1000:
		result += dict[1000]
	else:
		try:
			result += dict[(num/100)] + dict[100]
		except KeyError: 
			try:
				result += dict[num]
			except KeyError:
				try:
					result += dict[(num-num%100)/100] + 'hundred' + 'and' + dict[num%100]
				except KeyError:
					try:
						result += dict[(num-num%100)/100] + 'hundred' + 'and' + dict[num%100 - num%10] + dict[(num%10)]
					except KeyError:
						try:
							result += dict[(num-num%100)/100] + 'hundred' + 'and' + dict[(num%10)]
						except KeyError:
							try:
								result += dict[(num-num%100)/100] + 'hundred' + 'and' + dict[(num%100)]
							except KeyError:
								try:
									result += dict[num-num%10] + dict[num%10]
								except KeyError:
									print('Number out of range')
	return result

def main():
	numbs = numdict()
	sum = 0
	print(n2w(112, numbs))

	for i in range(1, 1001):	
		sum += len(n2w(i, numbs))
	print(sum)

if __name__ == '__main__':
	main()
