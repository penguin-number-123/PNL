def type_error(func,itype):
  if isinstance(itype,list):
    res = ""
    for i in range(len(itype)-2):
      res+= f"{itype[i]},"
    res+=f"{itype[-2]} and {itype[-1]}"
    raise Exception(f"{func.__name__} only allows types {res}.")
  else:
    raise Exception(f"{func.__name__} only allows type {itype}.")