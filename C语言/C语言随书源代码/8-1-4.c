int Age(int  n)
{ 
	int c;
	if (n == 1) 
	    c = 10;
	else  
            c = Age(n ¨C 1) + 2;
	return(c);
}
