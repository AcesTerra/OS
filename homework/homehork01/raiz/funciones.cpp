#include <stdio.h>      /* printf, scanf, NULL */
#include <stdlib.h>     /* malloc, free, rand */
#include <cstring>      /* memcpy */
#include <iostream>
#include <string>
#include <sstream>
#include "estructuras.cpp"
#include "headers.h"

using namespace std;

struct data extractData(char fileName[])
{
	char eof;
	char folder[] = "datos/";
	strcat(folder, fileName);
	char lineRead[50];
    	FILE *file;
    	if ((file = fopen(folder, "r")) == NULL) {
        	printf("Error! opening file");
        	// Program exits if file pointer returns NULL.
        	exit(1);
    	}

	//Extracting data from file
	int x, y;
	double z;
	char name[50];
	fscanf(file, "%d %d %lf %s", &x, &y, &z, name);
    	fclose(file);

	//Structure to store data
	data *a;
	int dataSize = sizeof(data);
	a = (struct data*) malloc(dataSize);
	a->x = x;
  	a->y = y;
  	a->z = z;
	memcpy(a->name, name, strlen(name) + 1);

	return *a;
}
