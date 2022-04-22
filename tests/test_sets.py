import time
import numpy as np
import PNL as p

t = time.time()
test = p.PNLset(1,2,3,4,4,5)
tt = time.time()
print(tt-t)
print(test)
t = time.time()
print(test.index(4))
tt = time.time()
print(tt-t)
print(test[test.index(4)])
try:
  print(test[9999])
except Exception as e:
  print(e)
test2 = p.PNLset(1,1,2,3,4,5)
print(test2)
test3 = p.PNLset(1,2,3,4)
print(test == test2)
print(test==test3)
print(p.to_set(list(range(100))))
np.set_printoptions(20)
print(np.e)