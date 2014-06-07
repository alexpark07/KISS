#include <stdio.h>

int main()
{
	int a;
	int *pa;
	int **ppa;

	pa = &a;
	ppa = &pa;

	a = 3;

	printf("a  : %08x, *pa: %08x, **pa: %08x\n", a, *pa, **ppa);
	printf("&a : %08x,  pa: %08x,  *pa: %08x\n", &a, pa, *ppa);
	printf("&pa: %08x, ppa: %08x\n", &pa, ppa);

	return 0;
}
