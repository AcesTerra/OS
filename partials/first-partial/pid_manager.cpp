#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int MIN_PID = 300;
int MAX_PID = 5000;
int PID_RANGE = MAX_PID - MIN_PID;
int pidMap[4700];

struct pid{
	int id;
	char name[50];
};

pid mapInfo[4700];

int allocate_map() {
	for(int i = 0; i < PID_RANGE; i++) {
		pidMap[i] = 0;
	}
	if(pidMap[4700] == 0)
		return 1;
	else
		return -1;
}

int allocate_pid(char name[]) {
	bool allocation = false;
	for(int i = 0; i < PID_RANGE; i++) {
		if(pidMap[i] == 0) {
			pidMap[i] = 1;
			(mapInfo+i) -> id = i + MIN_PID;
			memcpy((mapInfo+i), name, strlen(name) + 1);
			allocation = true;
			printf("Allocation ID: %d \n", i + MIN_PID);
			return i + MIN_PID;
		}
	}
	if (allocation == true)
		return 1;
	else
		return -1;
}
void release_pid(int pid) {
	pidMap[pid - MIN_PID] = 0;
	(mapInfo+pid - MIN_PID) -> id = 0;
	char name[] = " ";
	memcpy((mapInfo+pid - MIN_PID), name, strlen(name) + 1);
	//(mapInfo+pid - MIN_PID) -> name = "";
}

void showInfo(int pid){
	//printf("%d", pid-MIN_PID);
	printf("ID: %d, Name: %s\n", (mapInfo+pid-MIN_PID) -> id, (mapInfo+pid-MIN_PID) -> name);
}

int main(){
	int allocation = allocate_map();
	char test[] = "Prueba 1";
	allocate_pid(test);
	char test2[] = "Prueba 2";
	allocate_pid(test2);
	showInfo(300);
	showInfo(301);
	release_pid(300);
	showInfo(300);
	printf("%d\n", pidMap[0]);
	printf("%d\n", pidMap[1]);
	printf("%d\n", pidMap[0]);
	return 0;
}
