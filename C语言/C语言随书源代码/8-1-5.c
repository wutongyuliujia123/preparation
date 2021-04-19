long  Fac(int n)
{
    long f;
    if(n == 0) 
	f = 1;
    else 
	f = Fac(n - 1) * n;
    return(f);
}

int  main()
{
    int n;
    long fac;
    printf("\ninput a inteager number:");
    scanf("%d", &n);
    fac = Fac(n);
    printf("%d! = %ld\n", n, fac);
    return 0 ;
}
