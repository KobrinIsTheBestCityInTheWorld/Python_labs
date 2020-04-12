import math


def leonardo (n):
	if not isinstance(n, int):
		raise NameError('n must be int')
	if n<0 :
		raise ValueError('n must be positive')
	if n == 0 or n == 1:
		return 1
	b = (1 + math.sqrt(5))/2
	number = 2*(b**(n + 1) - (1 - b)**(n + 1))/(b - (1 - b)) - 1
	return int (number)


if __name__ == '__main__':
  	print (leonardo(3))