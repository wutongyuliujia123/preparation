#include <stdio.h>

int  * f()
{
    int n = 100;
    return &n;
}

int main()
{
    int *p = f();
    printf("Hello��\n");    //������һ�����
    printf("value = %d\n", *p);
    return 0;
}
