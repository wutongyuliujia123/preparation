#include<stdio.h>
int main()
{
	char st[20] = "C  program";
	char *ps = st;

	printf("%s\n", st);    //�������������
	printf("%s\n", ps);    //�������ָ�����
	printf("%s\n", "C program");    //��������ַ�������
	printf("%s\n", st + 3);    //�������ĳ��Ԫ�ص�ַ
	printf("%s\n", &ps[4]);    //�������ĳ��Ԫ�ص�ַ
	return 0;
}
