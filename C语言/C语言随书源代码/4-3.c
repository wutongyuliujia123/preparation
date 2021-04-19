#include <stdio.h>
int main(void)
{
    int i=8;
    printf("The raw value: i=%d\n", i);
    printf("++i=%d \n++i=%d \n--i=%d \n--i=%d\n",++i,++i,--i,--i);
    return 0;
}
