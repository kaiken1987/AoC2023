
#f = open("example.txt", "r")
f = open("input.txt", "r")
class maps_c:
   name:str = ""
   src = []
   dest = []
   def __init__(self) -> None:
      self.name = ""
      self.src = []
      self.dest = []
   def seed2dest(this, seed:int):
      for i in range(len(this.src)):
         if seed in this.src[i]:
            return seed-this.src[i].start+this.dest[i].start
      return seed
   
def loadSeeds(f) :
   line = f.readline()
   seeds = line.split(": ")[1].split()
   seeds =[int(x) for x in seeds]
   print( f"Seeds: {seeds}")
   line = f.readline()
   
def loadMaps(f) :
   curr=maps_c()
   maps = []
   for line in f:
      line = line.strip()
      if(not line):
         if(curr.name):
            maps.append(curr)
         curr=maps_c()
      elif( not curr.name ):
         curr.name = line
      else :
         dest, src,ran = line.split(maxsplit=3)
         dest = int(dest)
         src = int(src)
         ran = int(ran)
         curr.dest.append(range(dest,dest+ran))
         curr.src.append(range(src,src+ran))
   if(curr.name):
      maps.append(curr)
   return maps
      
def part1():
   print( "Part 1")
   seeds = loadSeeds(f)
   maps = loadMaps(f)
   
   for m in maps:
      for i in range(len(seeds)):
         seeds[i]= m.seed2dest(seeds[i])
      print( f"{m.name}: {seeds}")
   seeds.sort()
   print( f"locations: {seeds}")
   
def part2():
   print( "Part 2")
   
part1()
part2()
