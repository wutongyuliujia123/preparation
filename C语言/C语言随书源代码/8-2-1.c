int  Count() 
{
	static int  b = 0;    /* ������һ���ֲ���static���� */  
	b++; 
 	return b;
}
int  main()  
{  
	int a = 0;  
	a = Count (); /* a��ֵ����1 */ 
	a = Count (); /* a��ֵ����2 */  
	a = Count (); /* a��ֵ����3 */ 
	printf(��a = %d\n��, a);
	return 0;
}
