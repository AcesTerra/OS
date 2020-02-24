# multi_threaded.py
import time
from threading import Thread

C = 50000000

def cuentaRegresiva(n):
    while n>0:
        n -= 1

t1 = Thread(target=cuentaRegresiva, args=(C//2,))
t2 = Thread(target=cuentaRegresiva, args=(C//2,))

start = time.time()
t1.start()
t2.start()
t1.join()
t2.join()
end = time.time()

print('Tiempo de ejecución -', end - start)

