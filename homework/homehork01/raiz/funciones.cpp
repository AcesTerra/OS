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

	int x, y;
	double z;
	char name[50];
	//fscanf(file, "%d %d %lf %s", &x, &y, &z, name);
    	//Reads text until newline is encountered
    	//while((eof=fgetc(file)) != EOF){
		fscanf(file, "%d %d %lf %s", &x, &y, &z, name);
		//fscanf(file, "%[^\n]", x);
		//fscanf(file, "%[^\n]", y);
		//fscanf(file, "%[^\n]", z);
		//fscanf(file, "%[^\n]", name);
		//printf("Data from the file: %d %d %0.2lf %s\n", x, y, z, name);
	//}
    	fclose(file);
	data *a;
	int dataSize = sizeof(data);
	a = (struct data*) malloc(dataSize);
	a->x = x;
	//cout << "Entered to extract data" << endl;
  	a->y = y;
  	a->z = z;
	//char tempName[] = "Ecole que dijo";
	//cout << tempName << endl;
	//tempName = "Ecole que dijo";
	//a->nombre[50] = *tempName;
	memcpy(a->name, name, strlen(name) + 1);

  	//b.x = 1;
  	//b.y = 1;
  	//b.res = 2.7;

  	//todo[0] = *a;
  	//todo[1]= b;

	//cout << a->x << ", " << a->y << ", " << a->z << ", " << a->name << endl;
  	/*printf("%d,%d,%f\n", (todo+1)->x, (todo+1)->y, (todo+1)->res);

  	char *buffer;
  	buffer = (char*) malloc (2*ds);
  	memcpy(&buffer, &todo, 2*ds);

  	data *recover;
  	recover = (struct data*) malloc(2*ds);
  	memcpy(&recover, &buffer, 2*ds);

  	printf("%d,%d,%f\n",recover->x,recover->y,recover->res);
  	printf("%d,%d,%f\n",(recover+1)->x,(recover+1)->y,(recover+1)->res);*/

	return *a;
}
