import multiprocessing as mp

list_a = [[1, 2, 3], [5, 6, 7, 8], [10, 11, 12], [20, 21]]
list_b = [[2, 3, 4, 5], [6, 9, 10], [11, 12, 13, 14], [21, 24, 25]]
def same(a,b):
   c = [t for t in a if t in b]
   print(mp.current_process())
   return c

pool = mp.Pool(processes=4)
for a,b in zip(list_a, map(set, list_b)):
       result=pool.apply(same,args=(a,b) )
       print(result)
pool.close()
