#include <stdio.h>

//Build with: gcc -Wall -Werror -shared  -fPIC -o libprime.so prime.c

/*  From: http://stackoverflow.com/questions/7812044/finding-trailing-0s-in-a-binary-number
 *  Returns number of trailing zeros.
 *  d - number
 *  return number of starting zeros
 */
int numTrailingZeros(unsigned int d)
{
    unsigned int c = 32;
    d &= -1*((signed int)d);
    if (d) c--;
    if (d & 0x0000FFFF) c -= 16;
    if (d & 0x00FF00FF) c -= 8;
    if (d & 0x0F0F0F0F) c -= 4;
    if (d & 0x33333333) c -= 2;
    if (d & 0x55555555) c -= 1;
    return c;
}

/* Computes x^n % b
 * Borrowed from: literateprogams.org (in java)
 * Theory: http://en.wikipedia.org/wiki/Exponentiation_by_squaring sectio: Further applications
 */
int modularExponent(int x, int n, int b)
{
    long ans = 1;
    int i;
    for (i = 31; i >= 0; i--)
    {
        //a1a2 % n = b1b2 % n where b? = a? % n
        //Squaring for each power in the base, because we start with 1, higher order bits in power are irrelevant
        ans = (ans*ans) % b;
        //For each non-zero bit of power, get a base multiplied in there.
        if ((n & (1<<i)) != 0)
            ans = (ans*x) % b;
    }
    return (int) ans;
}

/* http://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
 * http://en.literateprograms.org/Miller-Rabin_primality_test_%28Java%29
 * Tests the two theorems:
 * a^d <not congruent with> 1 (mod n) AND
 * a^(2*rd) <not congruent with -1> (mod m) MEANS n NOT PRIME. Thus if one or the other succeeds,
 * there is a high probability that it is prime.
 *
 *
 */
char millerRabin(int a,int n)
{
    int i = 0;
    //Calculate "d", an odd value and s where 2^s * d = n-1
    //Easy: Start with n-1 and divide by two until it is odd (that is shift of triling 0's) and s is that number of divisions.
    int d = n-1;
    int s = numTrailingZeros((unsigned int)d);
    d >>= s;
    //Check first proposition
    int aD = modularExponent(a,d,n);
    if (aD == 1)
        return 1;
    for (i = 0; i < s-1; i++)
    {
        //n-1 is class -1,
        if (aD == n-1)
            return 1;
        aD = modularExponent(aD,2,n);
    }
    if (aD == n-1)
        return 1;
    return 0;
}

/* Prime test.  Calls Miller Rabin.
 * n - number to test primality for.
 */
char isPrime(int n)
{
    //1 is not prime, nor 0 nor anything below
    if (n <= 1)
        return 0;
    //2 Not caught by miller rabin.
    else if (n == 2)
        return 1;
    //Test cases put forth by Pomerance, Selfridge and Wagstaff[6] and Jaeschke (Wikipedia, see above)
    else if (millerRabin(2, n) && (n <= 7 || millerRabin(7, n)) && (n <= 61 || millerRabin(61, n)))
        return 1;
    return 0;
             
        
}
/* Test, generate 501 primes
 */
int main(int argc, char** argv)
{
    int i = 0;
    int cnt = 0;
    while (cnt <= 500)
    {
        if (isPrime(i))
        {    
            printf("%d, ",i);
            cnt++;
        }
        i++;
    }
    return 0;
}