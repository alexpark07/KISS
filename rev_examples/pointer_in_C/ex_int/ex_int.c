#include <stdio.h>

int main(void)
{
	int a;
	int *b;

	a = 10;
	b = &a;
	printf("a => %08x\n", a);
	printf("b => %08x\n*b ==> %08x\n", b, *b);
}
