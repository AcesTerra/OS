from multiprocessing import Pool
import time
import sys

#validLines = True
#validColumns = True
#validSquares = True

def checkLine(sudokuLine):
	isValid = True
	#global validLines
	#for lines in sudoku:
	#print(lines)
	lineSet = set(sudokuLine)
	#print(len(lineSet))
	if len(lineSet) < 9:
		isValid = False
	return isValid

def checkColumn(sudokuColumn):
	isValid = True
	#for lines in sudoku:
	#print(sudokuColumn)
	lineSet = set(sudokuColumn)
	#print(len(lineSet))
	if len(lineSet) < 9:
		isValid = False
	return isValid

def checkSquare(sudokuSquare):
	isValid = True
	#for lines in sudoku:
	#print(sudokuSquare)
	lineSet = set(sudokuSquare)
	#print(len(lineSet))
	if len(lineSet) < 9:
		isValid = False
	return isValid

if __name__ == '__main__':
	print("------------------------Sudoku------------------------")
	#print("Enter name of file to test")
	#fileName = str(input())
	args = list(sys.argv)
	fileName = args[1:]
	#print(fileName)
	file=open(fileName[0], "r")
	linesRead = file.readlines()
	file.close()
	#print(linesRead)
	linesWithoutEnter = []
	for i in linesRead:
		linesWithoutEnter.append(i[:len(i)-1])
	#print(linesWithoutEnter)
	sudoku = []
	for line in linesWithoutEnter:
		sudoku.append(list([int(x) for x in line]))
	print(sudoku)
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
	#print(sudoku)
	validLine1 = checkLine(sudoku[0])
	validLine2 = checkLine(sudoku[1])
	validLine3 = checkLine(sudoku[2])
	validLine4 = checkLine(sudoku[3])
	validLine5 = checkLine(sudoku[4])
	validLine6 = checkLine(sudoku[5])
	validLine7 = checkLine(sudoku[6])
	validLine8 = checkLine(sudoku[7])
	validLine9 = checkLine(sudoku[8])
	#print(validLine1)
	#print(validLine2)
	#print(validLine3)
	#print(validLine4)
	#print(validLine5)
	#print(validLine6)
	#print(validLine7)
	#print(validLine8)
	#print(validLine9)
	if validLine1 and validLine2 and validLine3 and validLine4 and validLine5 and validLine6 and validLine7 and validLine8 and validLine9:
		print("Lines checked: Correct")
	else:
		print("Lines checked: Incorrect")
	#transposedSudoku = list(map(list, zip(*sudoku)))
	#transposedSudoku = list(map(list,map(None,*sudoku)))
	transposedSudoku = [list(i) for i in zip(*sudoku)]
	#print(transposedSudoku)
	validColumn1 = checkColumn(transposedSudoku[0])
	validColumn2 = checkColumn(transposedSudoku[1])
	validColumn3 = checkColumn(transposedSudoku[2])
	validColumn4 = checkColumn(transposedSudoku[3])
	validColumn5 = checkColumn(transposedSudoku[4])
	validColumn6 = checkColumn(transposedSudoku[5])
	validColumn7 = checkColumn(transposedSudoku[6])
	validColumn8 = checkColumn(transposedSudoku[7])
	validColumn9 = checkColumn(transposedSudoku[8])
	#print(validColumn1)
	#print(validColumn2)
	#print(validColumn3)
	#print(validColumn4)
	#print(validColumn5)
	#print(validColumn6)
	#print(validColumn7)
	#print(validColumn8)
	#print(validColumn9)
	if validColumn1 and validColumn2 and validColumn3 and validColumn4 and validColumn5 and validColumn6 and validColumn7 and validColumn8 and validColumn9:
		print("Columns checked: Correct")
	else:
		print("Columns checked: Incorrect")
	square1 = []
	square2 = []
	square3 = []
	square4 = []
	square5 = []
	square6 = []
	square7 = []
	square8 = []
	square9 = []
	for i in range(3):
		for j in range(3):
			square1.append(sudoku[i][j])
	#print(square1)
	for i in range(3,6):
		for j in range(3):
			square2.append(sudoku[i][j])
	#print(square2)
	for i in range(6,9):
		for j in range(3):
			square3.append(sudoku[i][j])
	#print(square3)
	for i in range(3):
		for j in range(3,6):
			square4.append(sudoku[i][j])
	#print(square4)
	for i in range(3,6):
		for j in range(3,6):
			square5.append(sudoku[i][j])
	#print(square5)
	for i in range(6,9):
		for j in range(3,6):
			square6.append(sudoku[i][j])
	#print(square6)
	for i in range(3):
		for j in range(6,9):
			square7.append(sudoku[i][j])
	#print(square7)
	for i in range(3,6):
		for j in range(6,9):
			square8.append(sudoku[i][j])
	#print(square8)
	for i in range(6,9):
		for j in range(6,9):
			square9.append(sudoku[i][j])
	#print(square9)
	#validColumn1 = checkColumn(sudoku[:len(sudoku)-1][0])
	validSquare1 = checkSquare(square1)
	validSquare2 = checkSquare(square2)
	validSquare3 = checkSquare(square3)
	validSquare4 = checkSquare(square4)
	validSquare5 = checkSquare(square5)
	validSquare6 = checkSquare(square6)
	validSquare7 = checkSquare(square7)
	validSquare8 = checkSquare(square8)
	validSquare9 = checkSquare(square9)
	#print(validSquare1)
	#print(validSquare2)
	#print(validSquare3)
	#print(validSquare4)
	#print(validSquare5)
	#print(validSquare6)
	#print(validSquare7)
	#print(validSquare8)
	#print(validSquare9)
	if validSquare1 and validSquare2 and validSquare3 and validSquare4 and validSquare5 and validSquare6 and validSquare7 and validSquare8 and validSquare9:
		print("Square checked: Correct")
	else:
		print("Square checked: Incorrect")
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
