#Find the 10001 prime
from ctypes import *
from math import log10

#rotates a number
def rotate(num):
    digit = num % 10
    tmp = num // 10
    len = int(log10(num)) 
    tmp = tmp + int(digit * pow(10,len))
    return tmp
#Fast Miller-Rabin Prime library for 32-bit nums
#Programed by LeStarch
lib = cdll.LoadLibrary("libprime.so");

circ = [2,3]
sum = 5 #2,3 are prime but not for form 6k +,- 1
add = -1 #5 starts on -1
k = 1 #Come integer, any integer
#Loop through all possible primes
while  (6*k+add) < 1000000: 
    test = 6*k+add
    fail = False
    if lib.isPrime(test):
       tmp = rotate(test)
       while tmp != test:
           if not lib.isPrime(tmp):
               fail = True
               break
           tmp = rotate(tmp)
       if not fail:
           circ.append(test)
    #Check both 6k -1 and 6k+1 before incrementing k
    k = (k + 1) if (add == 1) else k
    add = -1*add
print(len(circ))
