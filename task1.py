import math as m


def sqpr_decompozition():
	'''
	Функция считает сумму по заданным границам
	'''
	while True:
		try:
			massiv = list(map(int, input("Введите последовательность чисел").split()))
			break
		except:
			print("Массив должен быть из чисел")
	length = len(massiv)
	amount_of_cells = m.ceil(m.sqrt(length))
	new_massiv = [0] * amount_of_cells
	for i in range (length):
		new_massiv[i//m.ceil(length/amount_of_cells)] += massiv[i]
	while True:
		left = int(input("Введите левую границу"))
		right = int(input("Введите правую границу"))	
		if left >= 0 and left < length and right >= 0 and right < length:
			break
		else: print("Введите границу корректно")
	number_of_left_cell = left//m.ceil(length/amount_of_cells)
	number_of_right_cell = right//m.ceil(length/amount_of_cells)
	summa = 0
	if number_of_left_cell == number_of_right_cell:
		for i in range(left,right+1):
			summa += massiv[i]
	else:
		for i in range(number_of_left_cell+1,number_of_right_cell):
			summa += new_massiv[i] 
		for i in range(left,m.ceil(length/amount_of_cells) + m.ceil(length/amount_of_cells) * number_of_left_cell):
			summa += massiv[i]
		for i in range(m.ceil(length/amount_of_cells) * number_of_right_cell,right+1):
			summa += massiv[i]
	print(summa)


def sqpr_decompozition_file():
	'''
	Функция считает сумму из файла
	'''
	while True:
		try:
			read_file = open("task1.txt", "r")
			massiv = list(map(int, read_file.readline().split()))
			left,right = list(map(int, read_file.readline().split()))
			read_file.close()
			break
		except:
			print("Массив должен быть из чисел")
	length = len(massiv)
	amount_of_cells = m.ceil(m.sqrt(length))
	new_massiv = [0] * amount_of_cells
	for i in range (length):
		new_massiv[i//m.ceil(length/amount_of_cells)] += massiv[i]
	number_of_left_cell = left//m.ceil(length/amount_of_cells)
	number_of_right_cell = right//m.ceil(length/amount_of_cells)
	summa = 0
	if number_of_left_cell == number_of_right_cell:
		for i in range(left,right+1):
			summa += massiv[i]
	else:
		for i in range(number_of_left_cell+1,number_of_right_cell):
			summa += new_massiv[i] 
		for i in range(left,m.ceil(length/amount_of_cells) + m.ceil(length/amount_of_cells) * number_of_left_cell):
			summa += massiv[i]
		for i in range(m.ceil(length/amount_of_cells) * number_of_right_cell,right+1):
			summa += massiv[i]
	print(summa)


if __name__ == '__main__':
	a = input("Как хотите ввести данные?\n 1.Ввод через файл\n 2.Ввод через клавиатуру")
	if a == "1": sqpr_decompozition_file()
	elif a == "2": sqpr_decompozition()
	else: print("Правильное решение")