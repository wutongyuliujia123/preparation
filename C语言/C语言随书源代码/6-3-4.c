#include <stdio.h>  
#define   ROWS   9   
int main()  
{  
    int i, j;  
    for ( i = 1; i <= ROWS; ++i )   // ��ѭ�������������  
    {  
        for ( j = 1; j <= i; ++j )  // ��ѭ�������������  
        {  
            printf("%d*%d=%d ", i, j, i * j);   // ����˻�  
        }  
        printf("\n");               // ����  
    }  
    return 0;  
}
