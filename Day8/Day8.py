import primefac 


#f = open("example.txt", "r")
f = open("input.txt", "r")

def part1():
   print( "Part 1")
   route = f.readline()
   f.readline()   
   network = {}
   for line in f:
      start = line[0:3]               
      left = line[7:10]               
      right = line[12:15]
      network[start] = (left,right)
   pos = 'AAA'
   idx = 0   
   steps = 0   
   while(pos!='ZZZ'):   
      if(route[idx]=='\n'):
         idx = 0         
      if(route[idx]=='L'):
         pos = network[pos][0]
      else:
         pos = network[pos][1]
      idx = idx+1
      steps += 1
   print(f"A journey of {steps} steps")            
         
def testDone( pos : list)->bool:
   for p in pos:
      if(p[-1] != 'Z'):
         return False
   return True
   
def part2():
   print( "Part 2")
   route = f.readline()
   f.readline()   
   network = {}
   pos = []
   for line in f:
      start = line[0:3]
      if( start[2] == 'A'):
         pos.append(start)
      left = line[7:10]               
      right = line[12:15]
      network[start] = (left,right)
   cycles =[]   
             
   for p in pos:   
      idx = 0   
      steps = 0 
      while(p[-1] != 'Z'):      
         if(route[idx]=='\n'):
            idx = 0            
         if(route[idx]=='L'):
            p = network[p][0]
         else:
            p = network[p][1]
         idx = idx+1
         steps += 1
      cycles.append(steps)   
   steps = 1            
   for c in cycles:
      fac = list(primefac.primefac( c) )
      print(f"{c}: {fac}")      
      steps *= fac[0]
   print(f"A journey of {steps} steps") 
   
#part1()
part2()
