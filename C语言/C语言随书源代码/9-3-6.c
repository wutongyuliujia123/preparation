#include <stdio.h>

int  * f()
{
    int n = 100;
    return &n;
}

int main()
{
    int *p = f();
    printf("Hello！\n");    //增加了一条语句
    printf("value = %d\n", *p);
    return 0;
}
