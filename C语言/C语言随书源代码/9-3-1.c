#include <stdio.h>
void Swap1(int a, int b)
{
    int  temp;    //¡Ÿ ±±‰¡ø
    temp = a;
    a = b;
    b = temp;
}
int main()
{
    int a = 5, b = 9;
    Swap1(a, b);
    printf("a = %d, b = %d\n", a, b);
    return 0;
}
