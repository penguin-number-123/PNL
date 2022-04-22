import time
import PNL as p
l = []
for i in range(1000):
  t = time.time()
  p.sqrt(173)
  tt = time.time()
  l.append(tt-t)
print(sum(l)/len(l))
l = []
for i in range(1000):
  t = time.time()
  math.sqrt(173)
  tt = time.time()
  l.append(tt-t)
print(sum(l)/len(l))
l = []
for i in range(1000):
  t = time.time()
  np.sqrt(173)
  tt = time.time()
  l.append(tt-t)
print(sum(l)/len(l))
print(np.sqrt(173))
print(math.sqrt(173))
print(p.sqrt(173))
