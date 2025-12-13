
#include <stdio.h>

int main(void)
{
    int x;
    int y;

    printf("x: ");
    if (scanf("%d", &x) != 1)
        return 1;

    printf("y: ");
    if (scanf("%d", &y) != 1)
        return 1;

    printf("%i\n", x + y);

    return 0;
}