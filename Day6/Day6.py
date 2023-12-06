from ctypes import BigEndianStructure


class race:
	time = 0
	best = 0
	def __init__(self, t,d) -> None:
		self.time = t
		self.best = d	

#races = [race(7,9),race(15,40),race(30,200)]
races = [race(44,208),race(80,1581),race(65,1050),race(72,1102)]
		
#f = open("example.txt", "r")
#f = open("input.txt", "r")

def part1():
	print( "Part 1")
	product = 1	
	for r in races:	
		numways = 0		
		for i in range(1,r.time):
			if((r.time-i)*i>r.best):
				numways = r.time-i*2+1 				
				break			
		print(f"Race has {numways} ways to win")			
		product *= numways
	print(f"Answer is {product}")					
def part2():
	print( "Part 2")
   
part1()
part2()
