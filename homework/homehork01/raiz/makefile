all: executable

executable: main.o estructuras.o funciones.o
	g++ main.o estructuras.o funciones.o headers.h -o executable

main.o: main.cpp
	g++ -c main.cpp

estructuras.o: estructuras.cpp
	g++ -c estructuras.cpp

funciones.o: funciones.cpp
	g++ -c funciones.cpp

clean:
	rm *o executable

