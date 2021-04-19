#include <stdio.h>

int  * f()
{
    int n = 100;
    return  &n;
}

int  main()
{
    int *p = f();
    printf("value = %d\n", *p);
    return 0;
}
