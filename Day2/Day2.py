import re
f = open("input.txt", "r")

maxcubes ={'red':12, 'green':13,'blue':14}
def part1():
   print( "Part 1")
   sum = 0
   for line in f:
      pulls = re.split(": |; |\n", line)
      valid = True
      for pull in pulls[1:]:
         dice = re.split(', | ', pull)
         #dice = pull.split(' ,')
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

part1()