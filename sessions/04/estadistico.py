from multiprocessing import Pool
import time
import sys

class tasks:
	def __init__(self):
		self.prom = 0
		self.min= 0
		self.max= 0

prom = 0.0
mini = 0.0
maxi = 0.0
mediana = 0.0
desviacion = 0.0

def promedio(numbers, test):
	global prom
	contador=0
	for i in numbers:
		prom = prom + int(i)
		contador = contador+1
	prom = prom / len(numbers)
	print("El promedio es:", prom)

def minimo(numbers, test):
	global mini
	tempa = 0.0
	conta=0
	for i in numbers:
		if conta == 0:
			tempa = numbers[conta]
			mini = tempa
		elif tempa > numbers[conta]:
			tempa = numbers[conta]
			mini = tempa
		conta = conta + 1
	print("El minimo es:", mini)

def maximo(numbers, test):
	global maxi
	temp = 0.0
	cont=0
	for i in numbers:
		if cont == 0:
			temp = numbers[cont]
			maxi = temp
		elif temp < numbers[cont]:
			temp = numbers[cont]
			maxi = temp
		cont = cont + 1
	print("El maximo es:", maxi)

def Mediana(numbers, test):
	global mediana
	Order = sorted(numbers)
	Len = len(numbers)//2
	cont = 0
	for i in Order:
		if cont == Len:
			mediana=Order[cont]
		cont+=1
	print("la mediana de los numeros es: -> ",mediana)

def Desviacion(numbers, test):
	global desviacion
	MedArit= 0.0
	cont=0.0
	for i in numbers:
		MedArit+=i
		cont+=1
	MedArit= MedArit/cont
	x=0
	for i in numbers:
		x += (i - MedArit)**2
	x = x/(cont-1)
	desviacion = math.sqrt(x)
	print("La desviacion estandar es de: -> ", desviacion)

if __name__ == '__main__':
	args = list(sys.argv)
	numbers = args[1:]
	obj = tasks()
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
