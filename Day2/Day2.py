import re
#f = open("example.txt", "r")
f = open("input.txt", "r")

def part1():
   print( "Part 1")
   maxcubes ={'red':12, 'green':13,'blue':14}
   sum = 0
   for line in f:
      pulls = re.split(": |; |\n", line)
      valid = True
      for pull in pulls[1:]:
         dice = re.split(', | ', pull)
         if(len(dice)==0):
            continue
         l = len(dice) // 2
         for i in range(l):
            color = dice[i*2+1]
            num = int(dice[i*2])
            if(num>maxcubes[color]):
               valid = False
               break
         if(valid==False):
            break
      print( pulls[0] + " " + str(valid))
      if(valid):
         sum += int(pulls[0][5:])
   print( f"Sum of valid {sum}")
   
def part2():
   print( "Part 2")
   sum = 0
   for line in f:
      pulls = re.split(": |; |\n", line)
      mincubes = {'red':0, 'green':0,'blue':0}
      for pull in pulls[1:]:
         dice = re.split(', | ', pull)
         if(len(dice)==0):
            continue
         l = len(dice) // 2
         for i in range(l):
            color = dice[i*2+1]
            num = int(dice[i*2])
            if(num>mincubes[color]):
               mincubes[color] = num
      power = 1
      for n in mincubes.values():
         power = power*n
      print( pulls[0] + " Power: " + str(power))
      sum += power
   print( f"Sum of Power {sum}")

part2()