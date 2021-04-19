#include "stdio.h"
int main()
{
	long a = 1, b = 1, n, i = 2;
	scanf("%d", &n);    //指定输出的个数
	printf("%10d%10d", a, b);
	for(; i < n; i = i + 2)
	{
   		a = a + b;
		b = b + a;
   		if(i%4 == 0)
			printf("\n");
   		printf("%10ld%10ld",a,b);
 	}
}
