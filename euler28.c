#include <stdio.h>
#include <math.h>
/*
Noticed the following:
1 + (sqip one less that 3*3) + (skip 3 less than 5*5)

Thus it is the sum of all values less than an odd square, skipping the previous 
odd square.
1 + (skipping 1 sum trhough
*/
int main(int argc,char** argv)
{
    int sqr = 1001;//(int)sqrt(1001);
    int last = 0;
    int i = 0;
    int val = 0;
    int sum = 0;
    for (i = 1; i <= sqr; i+=2)
    {
        //While less than current square
        while (val < i*i)
        {
            //Skip last square (add one makes it not a step)
            val += last+1;
            //and sum
            sum += val;
        }
        last = i;
    }
    printf("%d\n",sum);  

}
