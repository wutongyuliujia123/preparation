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

	//���庯��ָ��
	int (*p)(int, int);  //Ҳ����д��int (*p)(int a, int b)
	p = Max;  //��Max������ַ��ֵ��p��pָ��Max
	m = (*p)(x, y);   //�ȼ��� m = Max(x, y);
	printf("Max value = %d\n", m);

	p = Min;  //��Min������ַ��ֵ��p��pָ��Min
	m = (*p)(x, y);   //�ȼ��� m = Min(x, y);
	printf("Min value = %d\n", m);

	return 0;
}
