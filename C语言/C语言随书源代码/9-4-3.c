#include<stdio.h>
int main()
{
	char st[20] = "C  program";
	char *ps = st;

	printf("%s\n", st);    //输出项是数组名
	printf("%s\n", ps);    //输出项是指针变量
	printf("%s\n", "C program");    //输出项是字符串常量
	printf("%s\n", st + 3);    //输出项是某个元素地址
	printf("%s\n", &ps[4]);    //输出项是某个元素地址
	return 0;
}
