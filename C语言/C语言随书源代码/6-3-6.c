#include<stdio.h> 
int main() 
{     
	int i;     
	for(i = 51; i <= 150; i++)    
	{      
		if(i % 5 == 0)     
		{          
			printf("\n");  //ʹ�������ʾÿ�������һ�С�         
			continue;     
		}      
		printf("%5d",i);    
	}     
	printf("\n"); 
}
