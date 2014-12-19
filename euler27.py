#Find product a*b for |a| < 1000 |b| < 1000
#which yelds the longest consective run of prime numbers for n = 0..inf 
#From the following eqn 
#n^2 + an + b
from ctypes import *

#Fast Miller-Rabin Prime library for 32-bit nums
#Programed by LeStarch
lib = cdll.LoadLibrary("libprime.so");
runs = []
for a in range(-999,1000):
    for b in range(-999,1000):
        n = 0
        while lib.isPrime((n*n+a*n+b)):
            n = n + 1
        if n != 0:
            runs.append((n,a,b))
tup = max(runs)
print(tup[1]*tup[2])
