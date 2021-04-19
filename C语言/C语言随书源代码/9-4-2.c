#include<stdio.h>
int main()
{
	char st[20] = "C  program", *ps = "C  program";
	int i;
	
	for(i = 0; st[i] != '\0'; i++)    
	{
		if(st[i] == 'a')
		{
			printf("×Ö·û'a' ÔÚ×Ö·û´®ÖÐ\n");
			break;
		}
	}
 	if(st[i] == '\0')
		printf("×Ö·û'a' ²»ÔÚ×Ö·û´®ÖÐ\n");

	while(*ps != '\0')
	{
		if(*ps == 'a')
		{
			printf("×Ö·û'a' ÔÚ×Ö·û´®ÖÐ\n");
			break;
		}
		ps++;
	}
  	if(*ps == '\0')
		printf("×Ö·û'a' ²»ÔÚ×Ö·û´®ÖÐ\n");

	return 0;
}
