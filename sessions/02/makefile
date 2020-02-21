all: hello

hello: main.o funciones.o
	g++ main.o funciones.o -o proyecto1

main.o: main.cpp
	g++ -c main.cpp

funciones.o: funciones.cpp
	g++ -c funciones.cpp

clean:
	rm *o hello
