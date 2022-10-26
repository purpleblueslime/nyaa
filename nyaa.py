from sys import argv

def nyaaOpen(arg: str) -> str:
  try:
    with open(arg, 'r') as r: 
      return r.read()
  except: return 'Nothing here yet >,<'

o = nyaaOpen(argv.pop())
print(o)