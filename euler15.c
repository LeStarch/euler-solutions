#include <stdio.h>
int main(int argc, char** argv)
{
    int X = 21;
    int Y = 21;
    long vertex[X][Y];

    int i,j;     
    //zero our array
    for (i = 0; i < X; i++)
    {
        for (j = 0; j < Y; j++)
        {
            vertex[i][j] = 0;
        }
    }
    vertex[0][0] = 1; //Start with one path
    
    //Need to iterate accross the diagonals where x+y = const
    int sum = 0;
    //Counting stpes not paths
    for (sum = 0; sum <= (X-1+Y-1);sum++)
    {
        //Naieve solution, as problem space is small
        for (i = 0; i < X; i++)
        {
            for (j = 0; j < Y; j++)
            {
                if ((i + j) != sum)
                    continue;
                if (i-1 >= 0) 
                    vertex[i][j] += vertex[i-1][j];
                
                if (j-1>= 0) 
                    vertex[i][j] += vertex[i][j-1];
            }
        }
    }
    
    printf("%ld\n",vertex[X-1][Y-1]);
}
