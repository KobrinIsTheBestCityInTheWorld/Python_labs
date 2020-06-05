import math
import sys

def leonardo (n):
	if not isinstance(n, int):
		raise NameError('n must be int')
	if n < 0:
		raise ValueError('n must be positive')
	if n == 0 or n == 1:
		return 1
	b = (1 + math.sqrt(5))/2
	number = 2*(b**(n+1) - (1-b)**(n+1))/(b - (1-b)) - 1
	return int (number)

def main ():
	while True: 
		print ("Enter the number of Leonardo's number")
		n = int(input())
		try:
			print (leonardo (n))
		except: 
			print ("To big number")
		print ("One more time?")
		if input() == "No": 
			break

if __name__ == '__main__':
  	main()