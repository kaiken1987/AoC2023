
#f = open("example.txt", "r")
f = open("input.txt", "r")
def createHistory(values:list)->list:
   history = [values]
   while(history[-1].count(0)!=len(history[-1])):
      curr = []     
      for i in range(1,len(values)):
         curr.append(values[i]-values[i-1])
      history.append(curr)
      values = curr      
   history.reverse()
   return history
   
def predictNext( values :list )->int:
   history = createHistory(values)   
   pred = 0         
   for h in history:
      pred += h[-1]   
   return pred                        

def part1():
   print( "Part 1")
   sum = 0   
   for line in f:
      values = [int(x) for x in line.strip().split() ]
      next = predictNext( values )
      sum += next
   print(f"Sum of predictions {sum}")            
                      
   
def part2():
   print( "Part 2")
   
part1()
part2()
