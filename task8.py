import sys
import argparse 


def power_of_two (n):
	"""Определяет является ли число степенью 2


	Args: n -- число, которое проверяется
	Return: true -- является степенью 2
			false -- не является степенью 2


	"""
	if not isinstance(n, int):
		raise NameError('n must be int')
	if n <= 0:
		raise ValueError('n must be positive')
	if n & n-1 == 0:
		return True
	else:
		return False

def main ():
	parser = argparse.ArgumentParser()
	parser.add_argument("-n", type=int)
	args = parser.parse_args()
	if args.n is not None:
		try:
			print(power_of_two(args.n))
		except: 
			print("Error")
		print("One more time?")
		if input() in ["No","NO","no","nO","Нет","нет"]: 
			sys.exit()
	while True: 
		n = input("Enter the number: ")
		try:
			print(power_of_two(int(n)))
		except: 
			print("Error")
		print("One more time?")
		if input() in ["No","NO","no","nO","Нет","нет"]: 
			break

if __name__ == '__main__':
	main()