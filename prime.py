from ctypes import *

#Load the library
lib = cdll.LoadLibrary("libprime.so");

#Yields infinte list of primes
def primeGenerator():
    yield 2
    yield 3
    add = -1 #5 starts on -1
    k = 1 #Come integer, any integer
    #Loop through all possible primes
    while  True:
        test = 6*k+add
        if lib.isPrime(test):
            yield test
        #Check both 6k -1 and 6k+1 before incrementing k
        k = (k + 1) if (add == 1) else k
        add = -1*add
        
