#include <stdio.h>

int main(void)
{
	int arr[10] = { 100,98,97,95,89,76,92,96,100,99};
	
	int *parr = arr;
	int sum = 0;

	while( (parr - arr) <= 9 ) {
		sum += (*parr);
		parr++;
	}

	printf("average: %d\n", sum / 10);

	return 0;
}
