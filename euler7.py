#Find the 10001 prime
from ctypes import *

#Fast Miller-Rabin Prime library for 32-bit nums
#Programed by LeStarch
lib = cdll.LoadLibrary("libprime.so");

cnt = 2 #2,3 are prime but not for form 6k +,- 1
add = -1 #5 starts on -1
k = 1 #Come integer, any integer
prime = 3 #Most recent prime
#Loop through all possible primes
while  cnt < 10001:
    test = 6*k+add
    if lib.isPrime(test):
        cnt = cnt + 1
        prime = test
    #Check both 6k -1 and 6k+1 before incrementing k
    k = (k + 1) if (add == 1) else k
    add = -1*add
print(prime)
