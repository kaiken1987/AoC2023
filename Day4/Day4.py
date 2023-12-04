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
   return count

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
   cards = []
   total = 0
   for line in f:
      count = getWinCount(line)
      card = {'winCnt':count, 'copies':1}
      cards.append(card)
   for i in range(len(cards)):
      copies =cards[i]['copies']
      winCnt = cards[i]['winCnt']
      total += copies
      for j in range(i+1,i+winCnt+1):
         cards[j]['copies'] += copies
   print(f"Total Cards {total}")
   
#part1()
part2()
