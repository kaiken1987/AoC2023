
#f = open("example.txt", "r")
f = open("input.txt", "r")

class map_c:
	startx = -1
	starty = -1
	routes = []
	path = []	
	def addRow(self, line:str):
		row = []
		for x in line:         # 4
			if(x == '-'):      #1 2
				row.append(3)   # 8
			elif(x == 'J'):    
				row.append(5)
			elif(x == 'L'):    
				row.append(6)
			elif(x == '7'):    
				row.append(9)
			elif(x == 'F'):    
				row.append(10)
			elif(x == '|'):    
				row.append(12)
			elif(x == 'S'):    
				self.startx = len(row)
				self.starty = len(self.routes)	
				#row.append(10)#Example f  
				row.append(9)#input 7 
			else:
				row.append(0)								
		self.routes.append(row)
	def getNext(self, x, y, entry):
		curr = self.routes[y][x]
		curr = curr ^ entry
		if curr == 1:
			return (x-1,y,2)
		elif curr == 2:
			return (x+1,y,1)
		elif curr == 4:
			return (x,y-1,8)
		elif curr == 8:
			return (x,y+1,4)					
	def traverse(self) ->int:
		currx = self.startx
		curry = self.starty
		curr = self.routes[curry][currx]
		dir = 1			
		if (curr & 1) != 0:
			dir = 1				
		elif (curr & 2) != 0:
			dir = 2				
		elif (curr & 4) != 0:
			dir = 4
		else: 
			dir = 8
		steps = 1			
		currx,curry,dir = self.getNext(currx,curry,dir)
		self.path.append((currx,curry))
		while(currx!=self.startx) or (curry!=self.starty):
			currx,curry,dir = self.getNext(currx,curry,dir)
			self.path.append((currx,curry))			
			steps += 1			
		return steps					
mymap = map_c()
for line in f:
	mymap.addRow(line)	

def part1():
	print( "Part 1")	
	steps = (mymap.traverse())>>1 
	print( f"A journey of {steps} steps")	
							 
	
def part2():
	print( "Part 2")
	
part1()
part2()
	 
