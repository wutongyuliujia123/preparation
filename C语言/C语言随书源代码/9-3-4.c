void Inverse(int *arr, int n)  
{
	int temp, i, j, m = (n - 1) / 2;
	for(i = 0, j = n - 1; i <= m; i++, j--)
	{
	temp = arr[i];
	arr[i] = arr[j];
	arr[j] = temp;
	}
}

int  main()
{
	int i, a[]={3, 7, 9, 11, 0, 6, 7, 5, 4, 2};
	int len = sizeof(a) / sizeof(int);
	printf("原来的数组为:");
	for(i = 0; i < len; i++)
	printf("%d,", a[i]);
	printf("\n");
	Inverse(a, len);
	printf("逆置后数组为:");
	for(i = 0; i < len; i++)
	printf("%d,",a[i]);
	printf("\n");
	return 0;
}
