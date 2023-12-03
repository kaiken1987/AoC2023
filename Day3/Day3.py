
#f = open("example.txt", "r")
f = open("input.txt", "r")

def symidxs(line:str):
   out =[]
   for i in range(len(line)) :
      if(not(line[i] in '0123456789.')):
         out.append(i)
   return out
found = 0
foundParts = 0

def num_ranges(line:str):
   out = []
   curNum = 0
   curRange = range(-1,-1)
   global found
   for i in range(len(line)) :
      if(line[i].isdigit()):
         curNum = curNum*10+int(line[i])
         if(curRange.start==-1):
            curRange =range(i-1,i+2)
         else:
            curRange =range(curRange.start,i+2)                
      elif(curNum!=0):
         found += 1
         out.append( (curNum, curRange) )
         curNum=0;
         curRange = range(-1,-1)
       
   if(curNum!=0):
      found += 1
      out.append( (curNum, curRange) )
   return out

def checkInRange( r:range, idx)->bool:
   for i in idx:
      if(i in r):
         return True
   return False
ln = 0
def checks(currNums, previdx,curridx,nextidx) -> int:
   sum = 0
   global ln 
   ln+=1
   parts = []
   global foundParts
   for num in currNums:
      r = num[1]
      if( checkInRange(r,previdx) or checkInRange(r,curridx) or checkInRange(r,nextidx) ):
         sum += num[0]
         foundParts+=1
      else:
         parts.append(num[0])
            
   print( f"Line {ln}: sum {sum}, invalid parts {parts}")
   return sum

def part1():
   print( "Part 1")
   prevNums = []
   line = f.readline().strip()
   curridx = symidxs(line)
   currNums = num_ranges(line)
   sum = 0
   for line in f:
      line = line.strip()
      nextNums = num_ranges(line)
      
      sum += checks(curridx, prevNums, currNums, nextNums)
            
      prevNums = currNums
      currNums = nextNums
      curridx = symidxs(line)   
   
   sum += checks(currNums, previdx, curridx, nextidx)
            
   print( f"Found {foundParts}of{found} possible parts\nSum of parts {sum}")
   
def gearidxs(line:str):
   out =[]
   for i in range(len(line)) :
      if(line[i] == '*'):
         out.append(i)
   return out

def checks2(curridx,prevNums,currNums, nextNums) -> int:
   sum = 0
   nums = prevNums+currNums+nextNums
   for idx in curridx:
      ratio = 1
      count = 0
      for num in nums:
         if( idx in num[1]):
            count += 1
            ratio *= num[0]
      if(count==2):
         sum+=ratio
   return sum

def part2():
   print( "Part 2")
   prevNums = []
   line = f.readline().strip()
   curridx = gearidxs(line)
   currNums = num_ranges(line)
   sum = 0
   for line in f:
      line = line.strip()
      nextNums = num_ranges(line)
      
      sum += checks2(curridx, prevNums, currNums, nextNums)
            
      prevNums = currNums
      currNums = nextNums
      curridx = gearidxs(line)   
      
   sum += checks2(curridx, prevNums, currNums, nextNums)
   print( f"Sum of parts {sum}")
            
   
   
#part1()
part2()
   
