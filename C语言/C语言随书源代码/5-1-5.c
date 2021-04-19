#include <stdio.h>
int main()
{
    int a, b;
    printf("Input two numbers:");
    scanf("%d %d", &a, &b);
    if(a != b)
    {  
        if(a > b) printf("a>b\n");
        else      printf("a<b\n");
    }
    else
   {
        printf("a=b\n");
    }
    return 0;
}
