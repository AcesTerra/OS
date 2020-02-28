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
	validLine1 = checkLine(sudoku[0])
	validLine2 = checkLine(sudoku[1])
	validLine3 = checkLine(sudoku[2])
	validLine4 = checkLine(sudoku[3])
	validLine5 = checkLine(sudoku[4])
	validLine6 = checkLine(sudoku[5])
	validLine7 = checkLine(sudoku[6])
	validLine8 = checkLine(sudoku[7])
	validLine9 = checkLine(sudoku[8])
	validColumn1 = checkColumn(transposedSudoku[0])
	validColumn2 = checkColumn(transposedSudoku[1])
	validColumn3 = checkColumn(transposedSudoku[2])
	validColumn4 = checkColumn(transposedSudoku[3])
	validColumn5 = checkColumn(transposedSudoku[4])
	validColumn6 = checkColumn(transposedSudoku[5])
	validColumn7 = checkColumn(transposedSudoku[6])
	validColumn8 = checkColumn(transposedSudoku[7])
	validColumn9 = checkColumn(transposedSudoku[8])
	validSquare1 = checkSquare(square1)
	validSquare2 = checkSquare(square2)
	validSquare3 = checkSquare(square3)
	validSquare4 = checkSquare(square4)
	validSquare5 = checkSquare(square5)
	validSquare6 = checkSquare(square6)
	validSquare7 = checkSquare(square7)
	validSquare8 = checkSquare(square8)
	validSquare9 = checkSquare(square9)
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
