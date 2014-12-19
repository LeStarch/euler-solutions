#Find the 10001 prime
from ctypes import *

#Fast Miller-Rabin Prime library for 32-bit nums
#Programed by LeStarch
lib = cdll.LoadLibrary("libprime.so");

sum = 5 #2,3 are prime but not for form 6k +,- 1
add = -1 #5 starts on -1
k = 1 #Come integer, any integer
#Loop through all possible primes
while  (6*k+add) < 2000000: 
    test = 6*k+add
    if lib.isPrime(test):
        sum = sum + test
    #Check both 6k -1 and 6k+1 before incrementing k
    k = (k + 1) if (add == 1) else k
    add = -1*add
print(sum)
