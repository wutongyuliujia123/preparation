#include <stdio.h>                /* ͷ�ļ�*/
int max (int x, int y)     //�����ײ�
{  
int z;              //max���õ��ı���z,ҲҪ���Զ���
z = y;  
if (x > y) z = x;
return  z;         //��z��ֵ����,ͨ��max���ص��ô�
}

int main( )                    /* ������*/
{  
int a, b, c;                /*�������*/
scanf("%d, %d", &a, &b);    /*�������a��b��ֵ*/
c = max(a, b);              /*����max����,���õ���ֵ����c*/
printf("max = %d\n",c);     /*���c��ֵ*/
return 0;
}
