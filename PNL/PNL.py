import PNL.PNLerrors as e
def pow(x, y):
    if(y == 0): return 1
    temp = pow(x, int(y / 2))  
    if (y % 2 == 0):
        return temp * temp
    else:
        if(y > 0): return x * temp * temp
        else: return (temp * temp) / x
def root(n,b=2, l=0.0001) :
    x = n
    count = 0
    while (1) :
        count += 1
        root = 1/b * ((b-1)*x + (n / pow(x,b-1)))
        if (abs(root - x) < l) :
            break
        x = root
    return root
def sqrt(n, l=0.0001) :
    x = n
    count = 0
    while (1) :
        count += 1
        root = 0.5 * (x + (n / x))
        if (abs(root - x) < l) :
            break
        x = root
    return root
def to_set(x):
  if isinstance(x,list):
    return PNLset(*x)
  else:
    e.type_error(to_set,"list")
#special 1D set
class PNLset:
  def __init__(self,*args):
    self.as_set = set(args)
    self.__dict = {}
    self.__rev_dict = {}
    self.length = len(args)
    
    argsort = sorted(args)
    for i in range(len(args)):
      if not argsort[i] in self.__rev_dict.keys():
        self.__dict[i] = argsort[i]
        self.__rev_dict[argsort[i]] = i
  def __getitem__(self,indicies):
    if 0<=indicies < (self.length-1):
      return self.__dict[indicies] 
    else:
      raise Exception("Index for set is out of bounds")
  def __len__(self):
    return self.length
  def index(self,item):
    return self.__rev_dict[item]
  def __repr__(self):
    return "PNLset()"
  def __str__(self):
    res="{"
    for i in self.__dict.values():
      res+=f"{i},"
    res = res[:-1]+"}"
    return res
  def __eq__(self,other):
    return self.as_set==other.as_set
def set_zeros(x):
  return to_set([0]*x)

class Array:
  def __init__(self,shape,*args):
    pass