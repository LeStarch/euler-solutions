#Find the biggerst prime factor for num
from ctypes import *

#Fast Miller-Rabin Prime library for 32-bit nums
#Programed by LeStarch
lib = cdll.LoadLibrary("libprime.so");
num = 600851475143

add = -1 #5 starts on -1
k = 129192 #Come integer, any integer
prime = 3 #Most recent prime
#Loop through all possible primes
while  k > 1:
    test = 6*k+add
    if lib.isPrime(test):
        if num % test == 0:
            break
    #Check both 6k -1 and 6k+1 before incrementing k
    k = (k - 1) if (add == 1) else k
    add = -1*add
print(test)
