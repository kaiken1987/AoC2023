from itertools import count
import re
import math

#f = open("example.txt", "r")
f = open("input.txt", "r")

def getWinCount( line:str)->int:
   card,win,nums = re.split(": | \| ",line.strip(),3)
   win = win.split();
   nums = nums.split();
   count = 0
   for n in nums:
      if(n in win):
         count +=1

def part1():
   print( "Part 1")
   points = 0
   for line in f:
      count = getWinCount(line)
      if( count>0 ):
         points += math.pow( 2, count-1 )
   print(f"Total Points {points}")

def part2():
   print( "Part 2")
   
part1()
part2()
