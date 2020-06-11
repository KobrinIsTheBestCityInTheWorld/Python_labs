from alive_progress import alive_bar
import time


def Merge_it(stroka):
	if len(stroka) > 1:
		middle = len(stroka)//2
		left_side = stroka[:middle]
		right_side = stroka[middle:]
		mas = []
		a = Merge_it(left_side)
		b = Merge_it(right_side)
		counter_left = counter_right = 0
		while counter_left < len(a) and counter_right < len(b):
			if a[counter_left] < b[counter_right]:
				mas.append(a[counter_left])
				counter_left += 1
			else: 
				mas.append(b[counter_right])
				counter_right += 1 
		while counter_left < len(a):
			mas.append(a[counter_left])
			counter_left += 1
		while counter_right < len(b):
			mas.append(b[counter_right])
			counter_right += 1
		return mas
	else:
		return stroka


def main():	
	f = open("newfile.txt","w")
	t = open("text.txt", "r")
	massiv = t.read().split("\n")
	file_lines = []
	for i in range(len(massiv)):
		words_in_stroka = massiv[i].split()
		sortirovka = Merge_it(words_in_stroka)
		new_stroka = " ".join(sortirovka)
		file_lines.append(new_stroka)
	new_file_lines = Merge_it(file_lines)
	with alive_bar(len(new_file_lines)) as bar:
		for i in range(len(new_file_lines)):
			f.write(new_file_lines[i] + "\n")
			bar()
			time.sleep(0.005)
	f.close()
	t.close()


if __name__ == '__main__':
	main()




