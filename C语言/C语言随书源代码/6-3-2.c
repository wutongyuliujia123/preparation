#include "stdio.h"
void main()
{
	int s = 0, i = 1;
 	for(; i <= 100; s = s + i++) ;/*s=0+1+2+3+4+бн+100,i=101*/
	printf("i=%d,s=%d\n",i,s);
}
