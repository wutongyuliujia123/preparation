#include <stdio.h>

int Max(int a, int b)
{
	return a>b ? a : b;
}

int Min(int a, int b)
{
	return a<b?a:b;
}

int f(int (*p)(int, int), int x, int y)   //�������ĵ�һ���β��Ǻ���ָ��
{
	return (*p)(x, y);
}

int main()
{
	int x = 5, y = 9;
     
	printf("Max value = %d\n", f(Max, x, y));

	printf("Min value = %d\n", f(Min, x, y));

	return 0;
}
