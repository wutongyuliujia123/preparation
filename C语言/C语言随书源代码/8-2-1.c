int  Count() 
{
	static int  b = 0;    /* 定义了一个局部的static变量 */  
	b++; 
 	return b;
}
int  main()  
{  
	int a = 0;  
	a = Count (); /* a的值等于1 */ 
	a = Count (); /* a的值等于2 */  
	a = Count (); /* a的值等于3 */ 
	printf(“a = %d\n”, a);
	return 0;
}
