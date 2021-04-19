#include <stdio.h>

struct student
{
    int num;
    char *name;
    char sex;
    double score;
};

double Ave(struct student  *ps, int  n);

int main()
{
       struct student stus[] = {
        {12001, "Li Ming", 'M', 65},
        {12002, "Zhang Ping", 'M', 72.5},
        {12003, "Hua Fang",'F', 93},
        {12004, "Chen Ling",'F', 87},
        {12005, "Wang Xu",'M', 58}
      };
	struct student *ps = stus;	
	double average;
   
	average = Ave(ps, 5);
	printf("average = %f\n", average);

	return 0;
}

double Ave(struct student *ps, int n)
{
    double  ave, sum = 0;
    for(int i = 0; i < n; i++, ps++)
    {
        sum += ps->score;
    }
    ave = sum / n;
    return ave;
}
