import os                                                                       
import multiprocessing as mp
os.chdir('/home/manapati.m/csye7105/hw3_moukthika_manapati')
scripts = ('script1.py', 'script2.py', 'script3.py')  

def scriptsparallel(scripts):
      print('executed {}'.format(scripts))
      print(mp.current_process())
      os.system('python {}'.format(scripts))
    
pool = mp.Pool(processes=3)
args = [(script) for script in scripts]
pool.map(scriptsparallel, args)
pool.close()
