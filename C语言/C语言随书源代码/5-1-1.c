#include <stdio.h>
int main()
{
    int a, b, max;
    printf("��������������");
    scanf("%d %d", &a, &b);
    max = b;  // ����b���
    if(a > b)
    max = a;  // ���a>b����ô����max��ֵ
    printf("%d��%d�Ľϴ�ֵ�ǣ�%d\n", a, b, max);
    return 0;
}
