import math


#f = open("example.txt", "r")
f = open("input.txt", "r")

class hand:
   cards = []   
   bet = 0   
   strength = 0   
   def __init__(self,input:str,wilds:bool) -> None:
      input,bet = input.strip().split()   
      self.bet = int(bet) 
      self.cards = []              
      J = 11
      if wilds: J = 1            
      for i in input:
         if(i=='A'):
            self.cards.append(14)           
         elif(i=='K'):            
            self.cards.append(13)           
         elif(i=='Q'):            
            self.cards.append(12)           
         elif(i=='J'):            
            self.cards.append(J)           
         elif(i=='T'):            
            self.cards.append(10)           
         elif(i.isdigit()):            
            self.cards.append(int(i))
      self.strength = self.CalcStrength()           
   def CalcStrength(self)->float:
      cards = self.cards.copy()
      occur = {}
      result = 0     
      wilds = 0      
      for c in cards:
         if c==1:
            wilds += 1
         elif(c in occur):         
            occur[c]+=1
         else:
            occur[c]=1
         result = result*16+c
      result = result/(16**5)                     
      pairs = 0
      longest = 1                  
      for c in occur:
         if occur[c]>1:
            pairs+=1
            longest = max(longest,occur[c])
      longest += wilds
      if(pairs==1):
         if(longest==5):
            return result+6
         if(longest==4):
            return result+5
         if(longest==3):
            return result+3
         if(longest==2):
            return result+1
      elif(pairs==2):
         if(longest==3):
            return result+4#fullhouse
         if(longest==2):
            return result+2#2pair                     
      return result #highcard                                            
                             
                                           

def part1():
   print( "Part 1")
   hands = []   
   for line in f:
      hands.append(hand(line,False))
   hands.sort(key=lambda r: r.strenght,reverse=False)      
   winnings = 0
   for i in range(len(hands)):
      winnings += hands[i].bet*(i+1)    
   print(f"winnings {winnings}")                  
def part2():
   print( "Part 2")
   hands = []   
   f.seek(0) 
   for line in f:
      hands.append(hand(line,True))
   hands.sort(key=lambda r: r.strenght,reverse=False)      
   winnings = 0
   for i in range(len(hands)):
      winnings += hands[i].bet*(i+1)    
   print(f"winnings {winnings}")  
   
part1()
part2()
