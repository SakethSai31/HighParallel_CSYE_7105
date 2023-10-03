/* CSYE7105 HW1 Q2  */
/* Please parallelize this program with OpenMP */
/* Totals 15 points*/
#include <stdio.h>
#include <stdlib.h>
#include <omp.h>

#define N 10000

int main (int argc, char *argv[]) 

{

int nthreads, tid, i, chunk;

double a[N], b[N], c[N], t1, t2;
  
chunk = 10;
for (i=0; i < N; i++)
  a[i] = b[i] = i * 1.0;
/* Please set the follow block as parallel region;
   consider the data scope; and 
   set "dynamic" scheduling for the work-sharing for-loop 
   with the size of "chunk". */
t1 = omp_get_wtime();

#pragma omp parallel private (i, nthreads, tid) shared(chunk,a,b,c)

  {
  tid = omp_get_thread_num();
  if (tid == 0)
    {

    nthreads = omp_get_num_threads();
    printf("Number of threads = %d\n", nthreads);

    }

  printf("Thread %d starting...\n",tid);

  for (i=0; i<N; i++)
    {

    c[i] = a[i] + b[i];
    printf("Thread %d: c[%d]= %f\n",tid,i,c[i]);

    }
  }  /* end of parallel section */

t2 = omp_get_wtime();
double totaltime = t2 - t1
printf("Total Time %f ", totaltime);  

}