int main( )
{
	int  a, b, c ;
	scanf(“%d,%d”, &a, &b);
	c = Max(a, b);               /* 函数调用，a和b为实际参数*/
	printf(“Max is %d\n”, c);
	return 0;
}
