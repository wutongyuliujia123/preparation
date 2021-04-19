#include<stdio.h>
#define PI 3.14159265 
int main() 
{      
	int r;     
	float s;      
	for(r = 1;r <= 20; r++)     
	{      
		s = PI * r * r;      
		if(s > 200)
 			break;      
		printf("r=%d,s=%.2f\n", r, s);     
	}
    	 return 0;
}
