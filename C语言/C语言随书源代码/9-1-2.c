#include <stdio.h>
int main()
{
	int a = 15;
	int *p = &a;
	printf("%d, %d\n", a, *p);  //两种方式都可以输出a的值
	return 0;
}
