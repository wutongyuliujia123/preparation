#include "stdio.h"
int main()
{
		int r, a, b, lcm;
		scanf("%d %d", &a, &b);
		lcm = a * b;
		do
		{
			r = a % b;
			a = b;
			b = r;
		}while(r);
		printf("最小公倍数为%d", lcm / a);
     		return 0;
}
