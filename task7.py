import math
import sys
import argparse

def leonardo(n):
	"""Вычесляет число Леонардо


	Args: n -- номер числа, которое нужно вычеслить
	Return: n-ое число Леонардо


	"""
	if not isinstance(n, int):
		raise NameError('n must be int')
	if n < 0:
		raise ValueError('n must be positive')
	if n == 0 or n == 1:
		return 1
	b = (1 + math.sqrt(5))/2
	number = 2*(b**(n+1) - (1-b)**(n+1))/(b - (1-b)) - 1
	return int(number)

def main ():
	parser = argparse.ArgumentParser()
	parser.add_argument("-n", type=int)
	args = parser.parse_args()
	if args.n is not None:
		try:
			print(leonardo(args.n))
		except: 
			print("Error")
		print("One more time?")
		if input() in ["No","NO","no","nO","Нет","нет"]: 
			sys.exit()
	while True: 
		n = input("Enter the number: ")
		try:
			print(leonardo(int(n)))
		except: 
			print("Error")
		print("One more time?")
		if input() in ["No","NO","no","nO","Нет","нет"]: 
			break

if __name__ == '__main__':
	main()