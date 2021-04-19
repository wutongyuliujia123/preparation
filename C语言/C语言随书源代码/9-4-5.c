#include<stdio.h>
int main()
{
	char st[20] = "abcdefg";
	char *ps = "abcdefg";

	//scanf("%s", ps);     //此语句会造成运行错误
	//scanf("%s", "C program");  //同样此语句会造成运行错误

	scanf("%s", st);
	puts(st);

	return 0;
}
