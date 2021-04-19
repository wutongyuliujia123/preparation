SLIST  *Creat(int n) 
{
	SLIST  *pf, *pb, *head;
	int i;
	for(i=0;i<n;i++)
	{    
		pb = (SLIST *) malloc(sizeof(SLIST));
		printf("输入数据域整数：");
		scanf("%d", &pb ->data);
		pb ->next = NULL;
		if(i == 0)
			pf = head = pb;
		else 
			pf ->next = pb;
		pf = pb;
	}	
	return(head);
}
