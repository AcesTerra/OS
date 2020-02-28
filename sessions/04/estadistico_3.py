from multiprocessing import Pool
import time
import sys
import math

prom = 0.0
mini = 0.0
maxi = 0.0
mediana = 0.0
desviacion = 0.0

class simple:
        def __init__(self):
                self.i = 0

def promedio(numbers, test):
        global prom
        contador=0
        for i in numbers:
            prom = prom + int(i)
            contador = contador+1
        prom = prom / len(numbers)
        print("El promedio es: -> ",prom)

def minimo(numbers, test):
        global mini
        Min = sorted(numbers)
        mini=Min[0]
        print("El minimo es: -> ",mini)

def maximo(numbers, test):
        global maxi
        Max = sorted(numbers)
        cont=0
        for i in numbers:
            maxi = Max[cont]
            cont+=1
        print("El maximo es: -> ",maxi)

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
        print("La desviacion estandar es de: -> ",desviacion)


if __name__ == '__main__':
        args = list(sys.argv)
        numbers = args[1:]
        numbers = [ int(x) for x in numbers ]
        #numbers = [90,81,78,95,79,72,85]
        #print(numbers)
        test = simple()
        pool = Pool(processes=5)
        start = time.time()
        r1 = pool.apply_async(promedio, (numbers, test))
        r2 = pool.apply_async(minimo, (numbers, test))
        r3 = pool.apply_async(maximo, (numbers, test))
        r4 = pool.apply_async(Mediana, (numbers, test))
        r5 = pool.apply_async(Desviacion, (numbers, test))
        pool.close()
        pool.join()
        end = time.time()
        print('Tiempo de ejecución 1 es -> ', end - start)
