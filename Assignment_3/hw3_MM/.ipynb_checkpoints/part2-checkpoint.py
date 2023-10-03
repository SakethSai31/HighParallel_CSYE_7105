import pandas as pd
import numpy as np
import multiprocessing as mp
from time import time
random=np.random.rand(20000,100)
#random=np.random.randint(0,10,size=(20000,100))
df=pd.DataFrame(random*1000,index=np.arange(20000), columns=np.arange(100))
print(df)
def mse(df):
   #result=np.sqrt(sum([np.min(df,axis=0)**2,np.max(df,axis=0)**2]))
   result=np.sqrt(sum([np.min(df)**2,np.max(df)**2]))
   #print(mp.current_process())
   return result

def parallel(df):
    mseval=[]
    for i in range(df.shape[1]):
      #min,max=pool.apply(minmax,args=[df[i]])
      result=pool.apply(mse,args=[df[i]])
      mseval.append(result)
    print(mseval) 
    #return mse


elapsedtime=[]
speedup=[]
efficiency=[]
for processes in (1, 2, 4, 8):
  pool = mp.Pool(processes)
  t1 = time()
  parallel(df)
  pool.close()
  t2 = (time()-t1)
  print('\nPool Parallelism runs %0.3f seconds on %s CPUs.\n' % (t2, processes))
  elapsedtime.append(t2)
  speed=elapsedtime[0]/t2
  speedup.append(speed)
  print('\nspeed is ',speed, 'times on', processes, 'cpus')
  print('\n\n')
print(elapsedtime)

import seaborn as sns
import matplotlib.pyplot as plt

cpus = ['1','2','4','8']
fig = sns.lineplot(x=cpus, y=elapsedtime,color = 'firebrick')
fig.set(xlabel='CPUS', ylabel='Elapsed Time')
plt.savefig('/home/manapati.m/csye7105/hw3_moukthika_manapati/part2time.png')

cpus = ['1','2','4','8']
fig = sns.lineplot(x=cpus, y=speedup,color = 'firebrick')
fig.set(xlabel='CPUS', ylabel='Speed Up')
plt.savefig('/home/manapati.m/csye7105/hw3_moukthika_manapati/part2speedup.png')