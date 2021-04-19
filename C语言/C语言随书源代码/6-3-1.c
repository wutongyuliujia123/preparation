#include "stdio.h"
void main()
{
	int s, i;
 	for(s = 0, i = 1; i <= 100; i++)
		s = s + i;
 	printf("i=%d,s=%d\n", i, s);
}
