#include<stdio.h>
#include<stdlib.h>   //为了使用exit()
int main()
{
  FILE *fp;
  char ch;
  if((fp = fopen("d:\\a.txt", "w")) == NULL)
  {
    printf("Cannot open file\n");
    exit(1);
  }
  printf("input a string:");
  while ((ch = getchar()) != '\n')
  {
    fputc(ch, fp);
  }
  fclose(fp);

  if((fp = fopen("d:\\a.txt", "r")) == NULL)
  {
    printf("Cannot open file\n");
    exit(1);
  }  
  while((ch = fgetc(fp)) != EOF)
  {
    putchar(ch);
  }
  printf("\n");
  fclose(fp);

  return 0;
}
