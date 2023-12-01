f = open("input.txt", "r")


def part1():
   print( "Part 1")
   sum = 0
   for x in f:
      first = -1
      second = -1
      for c in x:
         if( c.isdigit() ):
            if(first<0):
               first = int(c)
            else :
               second = int(c)
            
      if(first>=0 and second<0 ):
         second = first
      if(first>=0 and second>=0 ):
         value = first*10+second;
         print(x + str( value ) )
         sum = sum +value;
      
   print( "Sum: " + str( sum ) )
def findReplace( a:str, b:str, replace:str ) -> str:
   if(len(a)<len(b)):
      return a[0]
   sub = a[:len(b)]
   if( sub != b ):
      return a[0]
   else:
      return replace
  


def comp(a:str, b:str) -> bool:
   if(len(a)<len(b)):
      return False
   sub = a[:len(b)]
   return sub == b
      
def str2digit(x:str) -> int:
   ns = ''
   i=0
   nums = [ ['one','1'],
           ['two','2'],
           ['three','3'],
           ['four','4'],
           ['five','5'],
           ['six','6'],
           ['seven','7'],
           ['eight','8'],
           ['nine','9']
           ]
   first = -1
   second = -1
   while( i <len(x)):
      v = -1
      if( x[i].isdigit() ):
         v = int(x[i])
      else:
         mini = x[i:]
         for num in nums:
            if( comp(mini,num[0]) ):
               v = int(num[1])
      if(v>=0): 
         if(first<0):
            first = v
         else :
            second = v 
      i += 1
   if(first<0):
      first = 0;
   if(second<0 ):
      second = first
   return first*10+second

      
   
def part2():
   print( "Part 2")
   sum = 0
   for s in f:
      first = -1
      second = -1
      value = str2digit(s.strip())
      print(s + ' ' + str( value ) )
      sum = sum +value;
      
   print( "Sum: " + str( sum ) )

   
#part1()
part2()