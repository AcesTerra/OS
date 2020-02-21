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
	if(argc != 2)
	{
		printf("Must have one argument\n");
		printf("Usage: ./main 4\n");
		printf("Parameter must be a digit\n");
		return 0;
	}

	//printf("%lu\n", sizeof(int));
	//printf("%lu\n", sizeof(double));
	//printf("%lu\n", sizeof(char[50]));

	int files = stoi(argv[1]);
	string extension = ".dat";
	data *allData;
  	int dataSize = sizeof(data);
  	//a = (struct data*) malloc(ds);
  	allData = (struct data*) malloc(dataSize*files);
	for(int i = 0; i < files; i++){
		string fileName = to_string(i+1) + extension;
		//cout << fileName << endl;
		char * charFileName = new char [fileName.length()];
		strcpy (charFileName, fileName.c_str());
		//allData[i] = extractData(fileNumber);
		//cout << "About to enter extractData" << endl;
		//allData[i] = extractData(charFileName);
		allData[i] = extractData(charFileName);
	}

	for(int i = 0; i < files; i++)
		printf("Data from the file %d.dat: %d %d %0.2lf %s\n", i+1, (allData+i)->x, (allData+i)->y, (allData+i)->z, (allData+i)->name);

	char *result;
  	result = (char*) malloc(dataSize*files);
  	memcpy(&result, &allData, dataSize*files);
	//printf("Data of result: %s\n", result);

	FILE *fptr;

	// opening file in writing mode
	fptr = fopen("resultados/datos.bin", "wb");

	// exiting program
	if (fptr == NULL) {
		printf("Error!");
		exit(1);
	}
	//cout << "Opening file" << endl;
	//printf("Enter a sentence:\n");
	//fgets(sentence, sizeof(sentence), stdin);
	//fprintf(fptr, "%s", result);
	fwrite(result, sizeof(result), 1, fptr);
	printf("%lu\n", sizeof(*allData));
	cout << "Writing into file" << endl;
	fclose(fptr);
	//cout << "Closing file" << endl;

	/*data *recover;
  	recover = (struct data*) malloc(dataSize*files);
  	memcpy(&recover, &result, dataSize*files);

	for(int i = 0; i < files; i++)
		printf("Data from recover %d: %d %d %0.2lf %s\n", i+1, (recover+i)->x, (recover+i)->y, (recover+i)->z, (recover+i)->name);*/

	//printf("%d,%d,%f\n",recover->x,recover->y,recover->res);
	//printf("%d,%d,%f\n",(recover+1)->x,(recover+1)->y,(recover+1)->res);
	return 0;
}
