from multiprocessing import Pool
import time
import sys

def checkLine(sudokuLine):
	isValid = True
	lineSet = set(sudokuLine)
	if len(lineSet) < 9:
		isValid = False
	return isValid

def checkColumn(sudokuColumn):
	isValid = True
	lineSet = set(sudokuColumn)
	if len(lineSet) < 9:
		isValid = False
	return isValid

def checkSquare(sudokuSquare):
	isValid = True
	lineSet = set(sudokuSquare)
	if len(lineSet) < 9:
		isValid = False
	return isValid

if __name__ == '__main__':
	print("------------------------Sudoku------------------------")
	print("Enter name of file to test")
	fileName = str(input())
	start = time.time()
	#args = list(sys.argv)
	#fileName = args[1:]
	file=open(fileName, "r")
	linesRead = file.readlines()
	file.close()
	linesWithoutEnter = []
	for i in linesRead:
		linesWithoutEnter.append(i[:len(i)-1])
	sudoku = []
	for line in linesWithoutEnter:
		sudoku.append(list([int(x) for x in line]))
	print("Este es tu sudoku:")
	print("-------------------------")
	for line in sudoku:
		print("|", end='')
		for number in range(9):
			if (number)%3 == 0 and number != 0:
				print(" | {0}".format(line[number]), end='')
			else:
				print(" {0}".format(line[number]), end='')
		print(" |", end='')

		print("\n-------------------------")
	transposedSudoku = [list(i) for i in zip(*sudoku)] #Transpose list to check columns
	square1 = []
	square2 = []
	square3 = []
	square4 = []
	square5 = []
	square6 = []
	square7 = []
	square8 = []
	square9 = []
	#Getting individual squares of sudoku
	for i in range(3):
		for j in range(3):
			square1.append(sudoku[i][j])
	for i in range(3,6):
		for j in range(3):
			square2.append(sudoku[i][j])
	for i in range(6,9):
		for j in range(3):
			square3.append(sudoku[i][j])
	for i in range(3):
		for j in range(3,6):
			square4.append(sudoku[i][j])
	for i in range(3,6):
		for j in range(3,6):
			square5.append(sudoku[i][j])
	for i in range(6,9):
		for j in range(3,6):
			square6.append(sudoku[i][j])
	for i in range(3):
		for j in range(6,9):
			square7.append(sudoku[i][j])
	for i in range(3,6):
		for j in range(6,9):
			square8.append(sudoku[i][j])
	for i in range(6,9):
		for j in range(6,9):
			square9.append(sudoku[i][j])
	pool = Pool(processes=27)
	start = time.time()
	t1 = pool.apply_async(checkLine, (sudoku[0],))
	validLine1 = t1.get(timeout=1)
	t2 = pool.apply_async(checkLine, (sudoku[1],))
	validLine2 = t2.get(timeout=1)
	t3 = pool.apply_async(checkLine, (sudoku[2],))
	validLine3 = t3.get(timeout=1)
	t4 = pool.apply_async(checkLine, (sudoku[3],))
	validLine4 = t4.get(timeout=1)
	t5 = pool.apply_async(checkLine, (sudoku[4],))
	validLine5 = t5.get(timeout=1)
	t6 = pool.apply_async(checkLine, (sudoku[5],))
	validLine6 = t6.get(timeout=1)
	t7 = pool.apply_async(checkLine, (sudoku[6],))
	validLine7 = t7.get(timeout=1)
	t8 = pool.apply_async(checkLine, (sudoku[7],))
	validLine8 = t8.get(timeout=1)
	t9 = pool.apply_async(checkLine, (sudoku[8],))
	validLine9 = t9.get(timeout=1)
	t10 = pool.apply_async(checkColumn, (transposedSudoku[0],))
	validColumn1 = t10.get(timeout=1)
	t11 = pool.apply_async(checkColumn, (transposedSudoku[1],))
	validColumn2 = t11.get(timeout=1)
	t12 = pool.apply_async(checkColumn, (transposedSudoku[2],))
	validColumn3 = t12.get(timeout=1)
	t13 = pool.apply_async(checkColumn, (transposedSudoku[3],))
	validColumn4 = t13.get(timeout=1)
	t14 = pool.apply_async(checkColumn, (transposedSudoku[4],))
	validColumn5 = t14.get(timeout=1)
	t15 = pool.apply_async(checkColumn, (transposedSudoku[5],))
	validColumn6 = t15.get(timeout=1)
	t16 = pool.apply_async(checkColumn, (transposedSudoku[6],))
	validColumn7 = t16.get(timeout=1)
	t17 = pool.apply_async(checkColumn, (transposedSudoku[7],))
	validColumn8 = t17.get(timeout=1)
	t18 = pool.apply_async(checkColumn, (transposedSudoku[8],))
	validColumn9 = t18.get(timeout=1)
	t19 = pool.apply_async(checkSquare, (square1,))
	validSquare1 = t19.get(timeout=1)
	t20 = pool.apply_async(checkSquare, (square2,))
	validSquare2 = t20.get(timeout=1)
	t21 = pool.apply_async(checkSquare, (square3,))
	validSquare3 = t21.get(timeout=1)
	t22 = pool.apply_async(checkSquare, (square4,))
	validSquare4 = t22.get(timeout=1)
	t23 = pool.apply_async(checkSquare, (square5,))
	validSquare5 = t23.get(timeout=1)
	t24 = pool.apply_async(checkSquare, (square6,))
	validSquare7 = t24.get(timeout=1)
	t25 = pool.apply_async(checkSquare, (square7,))
	validSquare6 = t25.get(timeout=1)
	t26 = pool.apply_async(checkSquare, (square8,))
	validSquare8 = t26.get(timeout=1)
	t27 = pool.apply_async(checkSquare, (square9,))
	validSquare9 = t27.get(timeout=1)
	pool.close()
	pool.join()
	if validLine1 and validLine2 and validLine3 and validLine4 and validLine5 and validLine6 and validLine7 and validLine8 and validLine9:
		print("Lines checked: Correct")
	else:
		print("Lines checked: Incorrect")
	if validColumn1 and validColumn2 and validColumn3 and validColumn4 and validColumn5 and validColumn6 and validColumn7 and validColumn8 and validColumn9:
		print("Columns checked: Correct")
	else:
		print("Columns checked: Incorrect")
	if validSquare1 and validSquare2 and validSquare3 and validSquare4 and validSquare5 and validSquare6 and validSquare7 and validSquare8 and validSquare9:
		print("Square checked: Correct")
	else:
		print("Square checked: Incorrect")
	end = time.time()
	print('Tiempo de ejecución es:', end - start)
	'''
	pool = Pool(processes=5)
	start = time.time()
	r1 = pool.apply_async(promedio, (numbers, obj))
	r2 = pool.apply_async(minimo, (numbers, obj))
	r3 = pool.apply_async(maximo, (numbers, obj))
	r4 = pool.apply_async(Mediana, (numbers, obj))
	r5 = pool.apply_async(Desviacion, (numbers, obj))
	pool.close()
	pool.join()
	end = time.time()
	print('Tiempo de ejecución es:', end - start)
	'''
