#include <stdio.h>
#define SIZE 45     //指定班级人数
void main()
{ 
	int score[SIZE], i, max;

	printf("输入%d个成绩值:\n", SIZE);
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

	printf("最高成绩 = %d\n", max);   
}
