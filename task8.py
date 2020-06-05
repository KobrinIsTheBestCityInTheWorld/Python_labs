import math
import sys

def power_of_two (n):
	if not isinstance(n, int):
		raise NameError('n must be int')
	if n <= 0:
		raise ValueError('n must be positive')
	if n & n-1 == 0:
		return True
	else:
		return False

def main ():
	while True: 
		print ("Enter the number")
		n = int(input())
		try:
			print (power_of_two (n))
		except: 
			print ("To big number")
		print ("One more time?")
		if input() == "No": 
			break

if __name__ == '__main__':
  	main()