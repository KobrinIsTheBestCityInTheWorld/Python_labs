import random
import string
from alive_progress import alive_bar
import time
import argparse


def words(size):
	"""Генерирует случайную послеловательность символов


	Args: size -- длина последовательности (слова)
	Return: word -- послеловательность символов (слово)
 

	"""
	word = ''
	for i in range(size):
		word += (random.choice(list(string.ascii_letters)))
	return word


def creat_file(Mb, K, L):
	"""Генерирует файл со словами


	Args: Mb -- размер файла
		  K -- диапозон, в котором определяется количество слов в строке
		  L -- диапозон, в котором определяется длина каждого слова
 

	"""
	if isinstance(Mb, int) and isinstance(K, tuple) and isinstance(L, tuple) and len(K) == 2 and len(L) == 2:
		Mb = 1024*1024*Mb
		f = open("text.txt", "w")
		i = 0
		with alive_bar(Mb) as bar:
			while i < Mb:
				nuber_of_word = random.choice(range(K[0],K[1]+1)) 
				for a in range(nuber_of_word):
					word_length = random.choice(range(L[0],L[1]+1))
					f.write(words(word_length) + " ")
					for s in range(word_length + 2):
						i += 1
						if i>= Mb:
							break
						bar()
				f.write("\n")
		f.close()
	else:
		print("Error") 

def main ():
	parser = argparse.ArgumentParser()
	parser.add_argument("-mb", type=int)
	parser.add_argument("-k", type=int, nargs="*", default=(10,100))
	parser.add_argument("-l", type=int, nargs="*", default=(3,10))
	args = parser.parse_args()
	creat_file(args.mb, tuple(args.k), tuple(args.l))
	

if __name__ == '__main__':
	main()