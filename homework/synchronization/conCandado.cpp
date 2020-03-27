#include <iostream>       // std::cout
#include <thread>         // std::thread
#include <unistd.h>       // std::usleep
#include <mutex>          // std::mutex
using namespace std;

mutex candado;

void imprime_x (int n, char x) {
    candado.lock();
    
    for (int i=0; i<n; ++i) 
      cout << x; 
    cout << '\n';

   candado.unlock();
}

int main ()
{
  //Creamos tres hilos que mandaremos a imprimir un símbolo diferente
  int threadNum = 3;
  int rep = 200;
  thread t[threadNum];
  char simbolos[] = "*#$";
  for (int i=0; i<threadNum; i++){
     t[i] = thread(imprime_x, rep, simbolos[i]);
  }
  for (int i=0; i<threadNum; i++)
     t[i].join();

  return 0;
}
