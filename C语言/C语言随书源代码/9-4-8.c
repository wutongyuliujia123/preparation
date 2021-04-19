unsigned int strlen(char  *s)
{
    char *p = s;
    while(*p != '\0')   //该循环将指针指向结尾字符’\0’
		p++;
    return p - s;
}


char  * strcpy(char *s1, char *s2)
{	
	char *p = s1;
	while((*p = *s2) != '\0') 
	{	
		p++;
		s2++;
	}	 
	return s1;
}

char  * strcat(char *s1, char *s2)
{
	char *p = s1;
	while(*p)
		p++;
	while(*p++ = *s2++)
	{
		;
	}
	return s1;
}

int strcmp(char *s1, char *s2)
{
	while(*s1 && *s2 && *s1 == *s2)
	{
		s1++;
		s2++;
	}
	return *s1 - *s2;
}

