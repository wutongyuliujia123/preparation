#include <stdio.h>
int main()
{
	int a = 15, b = 99, c = 222;
	int *p = &a;  //����ָ�����
	*p = b;  //ͨ��ָ������޸��ڴ��ϵ�����
	c = *p;  //ͨ��ָ�������ȡ�ڴ��ϵ�����
	printf("%d, %d, %d, %d\n", a, b, c, *p);
	return 0;
}
