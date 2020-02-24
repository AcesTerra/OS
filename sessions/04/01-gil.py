# single_threaded.py
import time
from threading import Thread

C = 50000000

def cuenta(n):
    while n>0:
        n -= 1

start = time.time()
cuenta(C)
end = time.time()

print('Tiempor de ejecución -', end - start)

