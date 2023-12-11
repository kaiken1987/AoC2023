
#f = open("example.txt", "r")
f = open("input.txt", "r")

def lineStr(row)->str:
	result = ""
	for c in row:
		if type(c) is str:
			result += c
		elif c >16:
			result += str(c)
		else:			
			result += ' '
	return result			

class map_c:
	startx = -1
	starty = -1
	routes = []
	path = []
	tubes = []	
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
			
	def __str__(self) -> str:
		result = ""
		for r in self.routes:
			result += lineStr(r)+"\n"	
		return result							
	
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
		self.tubes = [' '*len(x) for x in self.routes]		
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
		#self.tubes[curry]. [currx] = 'X'		
		while(currx!=self.startx) or (curry!=self.starty):
			currx,curry,dir = self.getNext(currx,curry,dir)
			self.path.append((currx,curry))
			#self.tubes[curry][currx] = 'X'			
			steps += 1			
		return steps	
	def insidePath(self):
		count = 0		
		for r, row in enumerate( self.routes ):
			line = ""			
			for c, item in enumerate(row):	
				inside = False
				on = False				
				for p in self.path:
					if(p[0] == c) and (p[1]==r):
						inside = False
						on = True
						break
					if(p[0] == c) and (p[1]<r) and (self.routes[p[1]][p[0]] &2):
						inside = not inside
				if (inside&1): 
					count += 1
					row[c] = 'O'
				elif(not on): row[c] = ' '
			print(f"{r+1000}: {lineStr(row)}")
		return count
			
mymap = map_c()
for line in f:
	mymap.addRow(line)	

def part1():
	print( "Part 1")	
	steps = (mymap.traverse())>>1 
	print( str(mymap) )	 
	print( f"A journey of {steps} steps")	
							 
	
def part2():
	print( "Part 2")
	inside = mymap.insidePath()
	print( f"{inside} points inside")	
	
part1()
part2()
	 
