def flatten_it(obj):
	try:
		for i in obj:
			if isinstance(i, str):
				yield i
			else:
				yield from flatten_it(i)
	except TypeError:
		yield obj
	except RecursionError:
		yield obj 

if __name__ == '__main__':
	L = [[[1, 2, 3], [4, 5]], 6, [[[['dog'],['world'],['python']],[7,8]]],[9],(45),{54}]
	print(list(flatten_it(L)))