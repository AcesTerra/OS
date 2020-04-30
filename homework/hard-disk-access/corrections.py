# coding: utf-8
#Esta función esta bien para leer el archivo pero si de aquí parten las funciones del programa es como si tuvieras dos main.
#Podría ser una función que lee el archivo y regresa la lista de líneas y después regresa al main y de ahí parten las demás funciones.
def FileReader():
    '''
    here the file is selected and read while separating into an array and sent to the functions <- Estos comentarios generalmente van por encima de la función y es una descripción general
    - FSFC -> First Come First Served  <- Si agregas la definición de las funciones tendría que se arriba de cada una.
    - SSTF -> Shortest seek time first
    '''

    ruta = "1.txt" # <- Utiliza todo en inglés o en español para los nombres de las variables

    file = open(ruta, 'r') # <- Estás utilizando la misma variable para guardar el archivo y para extraer las líneas

    file = file.readlines()

    FCFS(file) # <- Las funciones irían en el main
    SSTF(file)


def FCFS(file):
    '''
    First Come First Served <- Esto iría antes de la función y una descripción general de lo que hace
    :param file: are the numbers that are used to simulate the disks and cylinders of an HDD
    :return: the movements that the memory reader makes
    '''

    print("FCFS")
    print("First Come First Served")

    movements = 0

    start = file[0]
    end = file[1]

    for i in range(1, 1000, 1):

        cont = int(start) - int(end)

        if cont <= 0:
            cont = cont * (-1)

        movements = movements + cont
        start = file[i]
        end = file[i + 1]

    print("FCFS did", movements, "Movements!") # <- Checa el formato de salida que el profe nos pidió en la tarea


def SSTF(file):
    '''
    Shortest seek time first
    :param file: are the numbers that are used to simulate the disks and cylinders of an HDD
    :return: the movements that the memory reader makes
    '''
    print("SSTF")
    print("Shortest Seek Time First")

    variable = 0
    cont = 1000000
    movements = 0
    y = 0

    start = file[y]

    for i in range(1001):

        for x in range(1, 1000):

            distance = int(file[x]) - int(start)

            if distance <= 0:
                distance = distance * (-1)

            if distance < cont:
                variable = x
                cont = distance

        movements = movements + cont
        start = file[variable]
        file[y] = 10000000
        y = variable
        cont = 1000000

    print("SSTF did", movements, "Movements")


if __name__ == "__main__":
    '''
    call the file reader
    '''
    FileReader()
