#include <stdio.h>                /* 头文件*/
int max (int x, int y)     //函数首部
{  
int z;              //max函用到的变量z,也要加以定义
z = y;  
if (x > y) z = x;
return  z;         //将z的值返回,通过max带回调用处
}

int main( )                    /* 主函数*/
{  
int a, b, c;                /*定义变量*/
scanf("%d, %d", &a, &b);    /*输入变量a和b的值*/
c = max(a, b);              /*调用max函数,将得到的值赋给c*/
printf("max = %d\n",c);     /*输出c的值*/
return 0;
}
