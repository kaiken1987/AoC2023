import math
from unittest import skip

#f = open("example.txt", "r")
f = open("input.txt", "r")


def part1():
	print( "Part 1")
	universe = []
	for line in f:
		row = [x=='#' for x in line.strip()]		
		universe.append(row)		
	skipNext = False			
	for r, row in enumerate(universe):
		if(skipNext): 
			skipNext = False 
			continue
		if row.count(False) == len(row):
			skipNext = True
			universe.insert(r,row.copy())
	offset = 0;			
	for c in range(len(universe[0])):
		all = True
		for row in universe:
			if(row[c+offset]):
				all = False
				break			
		if(all):
			for row in universe:
				row.insert(c+offset, False)
			offset +=1													
	galaxies = []				
	for r, row in enumerate(universe):
		for c, item in enumerate(row):
			if(item):
				galaxies.append((r,c))
	sum = 0				
	for i in range(0,len(galaxies)):
		start = galaxies[i]		
		for j in range(i+1,len(galaxies)):		
			end = galaxies[j]
			dist = abs(start[0]-end[0])+abs(start[1]-end[1])
			sum += dist
			print(f"{i+1}-{j+1} = {dist}")
	print(f"Total paths: {sum}")									
						
	
def part2():
	print( "Part 2")
	
part1()
part2()
	 

