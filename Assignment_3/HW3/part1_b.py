import os
import multiprocessing as mp
os.chdir('/Users/sakethsai/Desktop/GIT Home/High Parallel/Assignment_3/HW3_Saketh')
scripts = ('script_1.py','script_2.py','script_3.py')

def parallelrun(scripts):
      print('executed {}'.format(scripts))
      print(mp.current_process())
      os.system('python {}'.format(scripts))
    
pool = mp.Pool(3)
args = [(script) for script in scripts]
pool.map(parallelrun, args)
pool.close()