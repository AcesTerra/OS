#include <sys/types.h>
#include <stdio.h>
#include <unistd.h>
int main()
{
    int i;
    for (i = 0; i < 4; i++){
	printf("Ecole\n");
	fork();
    }
    return 0;
}
