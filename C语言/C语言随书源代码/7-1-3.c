#include <stdio.h>
#define SIZE 45     //ָ���༶����
void main()
{ 
	int score[SIZE], i, max;

	printf("����%d���ɼ�ֵ:\n", SIZE);
	for(i = 0; i < SIZE; i++)
	{   
		printf("%d:", i + 1);
		scanf("%d", &score[i]);
	}

	max = score[0];
	for(i = 1; i < SIZE; i++)
	{  
		if(score[i] > max)   
		max = score[i];
	}

	printf("��߳ɼ� = %d\n", max);   
}
