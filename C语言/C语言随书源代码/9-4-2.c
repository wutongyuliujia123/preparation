#include<stdio.h>
int main()
{
	char st[20] = "C  program", *ps = "C  program";
	int i;
	
	for(i = 0; st[i] != '\0'; i++)    
	{
		if(st[i] == 'a')
		{
			printf("�ַ�'a' ���ַ�����\n");
			break;
		}
	}
 	if(st[i] == '\0')
		printf("�ַ�'a' �����ַ�����\n");

	while(*ps != '\0')
	{
		if(*ps == 'a')
		{
			printf("�ַ�'a' ���ַ�����\n");
			break;
		}
		ps++;
	}
  	if(*ps == '\0')
		printf("�ַ�'a' �����ַ�����\n");

	return 0;
}
