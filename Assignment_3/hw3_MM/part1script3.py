import multiprocessing as mp
import numpy as np
list_c = [[2, 3, 4, 5], [6, 9, 10, 12], [11, 12, 13, 14], [21, 24, 25, 26]]
def normalize(df):
    # Normalised [0,1]
    b = (df - np.min(df))/np.ptp(df)
    #print(b)
    return b.tolist()

pool = mp.Pool(4)
results = [pool.apply(normalize, args=(df, )) for df in list_c]
pool.close()    
print(results)

