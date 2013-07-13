# Roman Massey
# Computes and prints the 1,000th prime number

from math import *

# Check if n is prime
def isprime(n):
  prime = True
  if n % 2 == 0 and n!=2 or n%3==0 and n!=3:
    return False
  for divisor in range(2, n):
    if n % divisor == 0:
      prime = False
      break
  if prime == False:
    return False
  else:
    return True

lastnum = raw_input("Find sum of logarithms of all prime numbers from 2 to: ")

# Find the 1,000th prime number
counter = 1
sum = 0
for i in range(2,int(lastnum) + 1):
  if isprime(i):
    sum = sum + log(i)

print "Sum of logarithms of all prime numbers from 2 to "+str(lastnum)+": "+str(sum)


print "Ratio of n to sum of logs of primes: "+str(sum)+":"+str(lastnum)



