#include<stdio.h> 
int main() 
{     
	int i;     
	for(i = 51; i <= 150; i++)    
	{      
		if(i % 5 == 0)     
		{          
			printf("\n");  //使输出的显示每五个数换一行。         
			continue;     
		}      
		printf("%5d",i);    
	}     
	printf("\n"); 
}
