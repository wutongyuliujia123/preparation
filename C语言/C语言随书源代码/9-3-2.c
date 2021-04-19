#include<stdio.h>
void  Swap2(int *p1, int *p2)
{
	int  temp;
	temp = *p1;
	*p1 = *p2;
	*p2 = temp;
}
int  main()
{ 
	int a = 5, b = 9;
	int *pointer_1, *pointer_2;
	pointer_1 = &a;
	pointer_2 = &b;
	Swap2(pointer_1, pointer_2);
	printf("a = %d, b = %d\n",a,b);
	return 0;
}
