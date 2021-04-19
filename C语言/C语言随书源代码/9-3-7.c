#include <stdio.h>

int Max(int a, int b)
{
	return a > b  ?  a : b;
}
int Min(int a, int b)
{
	return a < b ? a : b;
}

int main()
{
	int x = 5, y = 9, m;

	//定义函数指针
	int (*p)(int, int);  //也可以写作int (*p)(int a, int b)
	p = Max;  //将Max函数地址赋值给p，p指向Max
	m = (*p)(x, y);   //等价于 m = Max(x, y);
	printf("Max value = %d\n", m);

	p = Min;  //将Min函数地址赋值给p，p指向Min
	m = (*p)(x, y);   //等价于 m = Min(x, y);
	printf("Min value = %d\n", m);

	return 0;
}
