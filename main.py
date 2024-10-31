# Griffin King
# Unit 3 Lab 2
# Doing factorial in three diferent ways, for, while, and recursion

from os import system
def main():
  num = 5
  print(f"<>----------------\n\n  For Loop:  {for_factorial(num)}\n\n")
  print(f"  While Loop:  {while_factorial(num)}\n\n")
  print(f"  Recursion:  {recursion_factorial(num)}\n\n<>----------------")

def for_factorial(num):
  numList = [ a for a in range(num+1) if a > 0] 
  num = 1
  for a in numList:
    num *= a
  return num

def while_factorial(num):
  numT = 1
  count = 1
  while count <= num:
    numT *= count
    count += 1
  return numT
    
def recursion_factorial(num):
  if num == 1:
    return num
  return recursion_factorial(num-1)*num  

if __name__ == "__main__":
  system("clear")
  main()
