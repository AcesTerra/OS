from multiprocessing import Pool
import time

C = 50000000
def cuenta(n):
    while n>0:
        n -= 1

if __name__ == '__main__':
    pool = Pool(processes=2)
    start = time.time()
    r1 = pool.apply_async(cuenta, [C//2]) #Divide la cuenta en 2
    r2 = pool.apply_async(cuenta, [C//2])
    pool.close()
    pool.join()
    end = time.time()
    print('Tiempo de ejecución -', end - start)

