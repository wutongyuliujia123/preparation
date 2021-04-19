#include <stdio.h>
int main(void)
{
  int a=15;
  float b=123.1234567;
  double c=12345678.1234567;
  char d='p';

  printf("a=%d\n", a);
  printf("a(%%d)=%d,a(%%5d)=%5d,a(%%o)=%o,a(%%x)=%x\n\n",a,a,a,a);  // %% ¿ÉÒÔÊä³ö %

  printf("a=%f\n", b);
  printf("b(%%f)=%f,b(%%lf)=%lf,b(%%5.4lf)=%5.4lf,b(%%e)=%e\n\n",b,b,b,b);

  printf("c=%f\n", c);
  printf("c(%%lf)=%lf, c(%%f)=%f, c(%%8.4lf)=%8.4lf\n\n",c,c,c);

  printf("d=%c\n", d);
  printf("d(%%c)=%c, d(%%8c)=%8c\n",d,d);
  return 0;
}
