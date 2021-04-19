#include <stdio.h>
int main()
{
	int    a = 10,   *pa = &a;
	double b = 99.9, *pb = &b;
	char   c = '@',  *pc = &c;	

	//最初的值
	printf("&a=%#X, &b=%#X, &c=%#X\n", &a, &b, &c);
	printf("pa=%#X, pb=%#X, pc=%#X\n", pa, pb, pc);
	//加法运算
	pa++; pb++; pc++;
	printf("pa=%#X, pb=%#X, pc=%#X\n", pa, pb, pc);
	//减法运算
	pa -= 2; pb -= 2; pc -= 2;
	printf("pa=%#X, pb=%#X, pc=%#X\n", pa, pb, pc);

	return 0;
}
