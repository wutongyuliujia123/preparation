void  Swap (int x,  int y)
{  
	int  temp;
	temp = x;  
	x = y;  
	y = temp;
	printf(¡°x=%d ,  y=%d  \n¡±,  x,  y);
}

int main()
{  
	int  a = 3, b = 5;
	Swap (a, b);    
	printf(¡°a=%d, b=%d\n¡±, a, b);
	return 0;
}
