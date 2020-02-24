from multiprocessing import Pool
import time
import sys

class tasks:
	def __init__(self):
		self.prom = 0
		self.min = 0
		self.max = 0

#prom = 0.0
#min = 0.0
#max = 0.0

def promedio(numbers, test):
	#sum = 0.0
	for i in numbers:
		test.prom = test.prom + int(i)
	test.prom = test.prom / len(numbers)
	#print(sum)
	#return sum

def minimo(numbers, test):
	numbers.sort()
	test.min = numbers[0]
	#print(numbers[0])
	#return numbers[0]

def maximo(numbers, test):
	#global max
	numbers.sort()
	test.max = numbers[len(numbers)]
	#print()
	#return numbers[len(numbers)]

if __name__ == '__main__':
	#args = list(sys.argv)
	#numbers = args[1:]
	numbers = [90,81,78,95,79,72,85]
	print(numbers)
	pool = Pool(processes=3)
	#start = time.time()
	obj = tasks()
	r1 = pool.apply_async(promedio, (numbers, obj)) #Divide la cuenta en 2
	r2 = pool.apply_async(minimo, (numbers, obj))
	r3 = pool.apply_async(maximo, (numbers, obj))
	pool.close()
	pool.join()
	#pool.join()
	#pool.join()
	#end = time.time()
	print("El promedio es: ", obj.prom)
	print("El minimo es: ", obj.min)
	print("El maximo es: ", obj.max)
	#print('Tiempo de ejecución -', end - start)

