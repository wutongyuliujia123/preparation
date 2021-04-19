#include <stdio.h>  
#define   ROWS   9   
int main()  
{  
    int i, j;  
    for ( i = 1; i <= ROWS; ++i )   // 外循环控制输出行数  
    {  
        for ( j = 1; j <= i; ++j )  // 内循环控制输出列数  
        {  
            printf("%d*%d=%d ", i, j, i * j);   // 输出乘积  
        }  
        printf("\n");               // 换行  
    }  
    return 0;  
}
