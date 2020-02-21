#include <stdio.h>      /* printf, scanf, NULL */
#include <stdlib.h>     /* malloc, free, rand */
#include <cstring>      /* memcpy */
#include <iostream>
#include <string>
#include <sstream>
#include "estructuras.cpp"
#include "headers.h"

using namespace std;

int main(int argc, char** argv)
{
	//Checking correct arguments
	if(argc != 2)
	{
		printf("Must have one argument\n");
		printf("Usage: ./main 4\n");
		printf("Parameter must be a digit\n");
		return 0;
	}

	//Initializing array of struct
	int files = stoi(argv[1]);
	string extension = ".dat";
	data *allData;
  	int dataSize = sizeof(data);
  	allData = (struct data*) malloc(dataSize*files);
	//Extract data from files
	for(int i = 0; i < files; i++){
		string fileName = to_string(i+1) + extension;
		char * charFileName = new char [fileName.length()];
		strcpy (charFileName, fileName.c_str());
		allData[i] = extractData(charFileName);
	}

	//Printing data extracted from files
	for(int i = 0; i < files; i++)
		printf("Data from the file %d.dat: %d %d %0.2lf %s\n", i+1, (allData+i)->x, (allData+i)->y, (allData+i)->z, (allData+i)->name);

	//Char array to copy data
	char *result;
  	result = (char*) malloc(dataSize*files);
  	memcpy(&result, &allData, dataSize*files);

	FILE *fptr;

	//Opening file in writing binary mode
	fptr = fopen("resultados/datos.bin", "wb");

	//Exiting program if file is not created
	if (fptr == NULL) {
		printf("Error!");
		exit(1);
	}

	fwrite(result, sizeof(result), 1, fptr);
	cout << "Writing into file" << endl;
	fclose(fptr);

	return 0;
}
