#include <stdlib.h>
#include <stdio.h>
#include <iostream>
#include <string.h>
#include <time.h>
#include <unistd.h>
#include <thread>
#include <mutex>
using namespace std;

int MAX_PID = 5000;
int  MIN_PID = 300;
int PID_RANGE = 4700;
int pid_map[4700];
int upper = 10;
int lower = 1;
mutex allocationLocker;
mutex releaseLocker;

int allocate_map();
int allocate_pid();
int release_pid(int pid);
void assign_pid();

int allocate_map() {
	for(int i = 0; i < PID_RANGE; i++) {
		pid_map[i] = 0;
	}
	return 1;
}

int allocate_pid() {
	allocationLocker.lock();
	for(int i = 0; i < PID_RANGE; i++) {
		if(pid_map[i] == 0) {
			pid_map[i] = 1;
			allocationLocker.unlock();
			printf("Allocation locker unlocked \n");
			return i + MIN_PID;
		}
	}
	return 1;
}

int release_pid(int pid) {
	releaseLocker.lock();
	pid_map[pid - MIN_PID] = 0;
	printf("Array released: %d\n", pid_map[pid - MIN_PID]);
	if (pid_map[pid - MIN_PID] == 0){
		releaseLocker.unlock();
		printf("Release locker unlocked\n");
		return 1;
	}
	else{
		releaseLocker.unlock();
		return 0;
	}
	return 0;
}

void assign_pid(){
	srand(time(0));
	int timeSleep = (rand() % (upper - lower + 1)) + lower;
	//printf("%d\n", timeSleep);
	printf("Allocate process\n");
	int process = allocate_pid();
	printf("ID assigned: %d\n", process);
	printf("Time to sleep: %d\n", timeSleep);
	sleep(timeSleep);
	int releasedResult = release_pid(process);
	if(releasedResult == 1)
		printf("PID %d released successfully\n", process);
	else
		printf("PID %d not released successfully\n", process);
}

int main(){
	printf("PID Manager\n");
	allocate_map();
	int threadNum = 100;
	thread t[threadNum];
	for (int i=0; i<threadNum; i++)
		t[i] = thread(assign_pid);
	for (int i=0; i<threadNum; i++)
		t[i].join();
	//assign_pid();
	return 1;
}
