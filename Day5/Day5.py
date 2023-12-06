
#f = open("example.txt", "r")
f = open("input.txt", "r")

def split(a,b:range): #break  up a where it intersects b
	if( (a.start==b.start and a.stop==b.stop) ): #
		return [a]
	elif( a.start<=b.start and a.stop>b.start ): #
		if( a.stop>b.stop): #a..b..b..a
			return [range(a.start,b.start),range(b.start,b.stop),range(b.stop,a.stop)]
		else: #a..b..a..b
			return [range(a.start,b.start),range(b.start,a.stop)]
	elif( a.start>=b.start and a.start<b.stop ): #b..a..b
		if( a.stop>b.stop): #b..a..b..a
			return [range(a.start,b.stop),range(b.stop,a.stop)]
	return[a]	
	
def intersect(a,b:range) -> bool: #break  up a where it intersects b
	if( (a.start==b.start and a.stop==b.stop) ): #
		return True
	elif( a.start<=b.start and a.stop>b.start ): #
		return True
	elif( a.start>=b.start and a.start<b.stop ): #b..a..b
		return True
	else:
		return False
	
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
	def seed2dest(this, seed:range) -> list:
		out = [seed] 
		for i in range(len(this.src)):
			src = this.src[i]
			curr = []
			for r in out:
				curr += split(r,src)
			out = curr.copy()
			curr =[r]
		mid = out.copy()
		out = []		
		for r in mid:
			if( r.start == r.stop):
				continue
			found = False
			for i in range(len(this.src)):
				src = this.src[i]
				dest = this.dest[i]
				if intersect(r, src):
					shift = dest.start-src.start
					out.append(range( r.start+shift,r.stop+shift ))
					found = True
					break
			if( not found):
				out.append(r)
		return out
					

def loadSeeds(f) :
	line = f.readline()
	seeds = line.split(": ")[1].split()
	seeds =[int(x) for x in seeds]
	print( f"Seeds: {seeds}")
	line = f.readline()
	return seeds
	
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
	

def part2():
	print( "Part 2")
	seeds = loadSeeds(f)
	maps = loadMaps(f)
	seeds2 = []
	for i in range(0,len(seeds),2):
		 seeds2.append( range(seeds[i],seeds[i]+seeds[i+1]) )
	seeds = seeds2.copy()
	for m in maps:
		seeds2= []
		for i in range(len(seeds)):
			seeds2 += m.seed2dest(seeds[i])
		seeds = seeds2.copy()
		print( f"{m.name}: {seeds}")
	seeds.sort( key=lambda r: r.start)
	print( f"locations: {seeds}")
	
#part1()
part2()
