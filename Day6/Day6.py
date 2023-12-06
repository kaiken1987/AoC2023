








import math


class race:
	time = 0
	best = 0
	def __init__(self, t,d) -> None:
		self.time = t
		self.best = d	
	def solve(self) -> int:
		sq = self.time*self.time+4*-self.best 		
		a = (-self.time-math.pow( sq, 0.5 ))/-2
		b = (-self.time+math.pow( sq, 0.5 ))/-2
		if( a<b ):
			return math.floor(b)-math.ceil(a)+1 
		else:		
			return math.floor(a)-math.ceil(b)+1 

#races = [race(7,9),race(15,40),race(30,200)]
races = [race(44,208),race(80,1581),race(65,1050),race(72,1102)]
		
#f = open("example.txt", "r")
#f = open("input.txt", "r")

def part1():
	print( "Part 1")
	races = [race(7,9),race(15,40),race(30,200)]
	#races = [race(44,208),race(80,1581),race(65,1050),race(72,1102)]
	product = 1	
	for r in races:	
		numways = r.solve()
		print(f"Race has {numways} ways to win")			
		product *= numways
	print(f"Answer is {product}")					
def part2():
	print( "Part 2")
	#races = [race(71530,940200)]
	races = [race(44806572,208158110501102)]
	product = 1	
	for r in races:	
		numways = r.solve()
		print(f"Race has {numways} ways to win")			
		product *= numways
	print(f"Answer is {product}")	
   
part1()
part2()
