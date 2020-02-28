'''
Class: Operating Systems
Assigment: Session04 Threads
Team: Alfredo Garcia, Jorge Chavez & Andre Ruiz
'''

from multiprocessing import Pool
import time
import sys
import math

prom = 0.0
mini = 0.0
maxi = 0.0
mediana = 0.0
desviacion = 0.0

def promedio(numbers):
        global prom
        contador=0
        for i in numbers:
            prom = prom + int(i)
            contador = contador+1
        prom = prom / len(numbers)
        return prom

def minimo(numbers):
        global mini
        Min = sorted(numbers)
        mini=Min[0]
        return mini

def maximo(numbers):
        global maxi
        Max = sorted(numbers)
        cont=0
        for i in numbers:
            maxi = Max[cont]
            cont+=1
        return maxi

def Mediana(numbers):
        global mediana
        Order = sorted(numbers)
        Len = len(numbers)//2
        cont = 0
        for i in Order:
          if cont == Len:
            mediana=Order[cont]
          cont+=1
        return mediana

def Desviacion(numbers):
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
        return desviacion


if __name__ == '__main__':
        args = list(sys.argv)
        numbers = args[1:]
        numbers = [ int(x) for x in numbers ]
        pool = Pool(processes=5)
        start = time.time()
        r1 = pool.apply_async(promedio, (numbers,))
        print("El promedio es: -> ", r1.get(timeout=1))
        r2 = pool.apply_async(minimo, (numbers,))
        print("El minimo es: -> ", r2.get(timeout=1))
        r3 = pool.apply_async(maximo, (numbers,))
        print("El maximo es: -> ", r3.get(timeout=1))
        r4 = pool.apply_async(Mediana, (numbers,))
        print("la mediana de los numeros es: -> ", r4.get(timeout=1))
        r5 = pool.apply_async(Desviacion, (numbers,))
        print("La desviacion estandar es de: -> ", r5.get(timeout=1))
        pool.close()
        pool.join()
        end = time.time()
        print('Tiempo de ejecución 1 es -> ', end - start)
