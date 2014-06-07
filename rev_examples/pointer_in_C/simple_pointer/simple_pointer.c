#include <stdio.h>
#include <stdint.h>
#include <string.h>

void func1()
{
	char buf[128] = { 0x00, };
	char *pbuf = buf;
	int offset = 0x0;

	strcpy(buf, "0123456789012345");
	printf("buf: %s\n", buf);

	printf("buf: ");
	while( (*pbuf) != '\0' ) {
		printf("%c", *pbuf);
		pbuf++;
	}
	printf("\n");

	pbuf = &buf[0];

	*(int32_t *)&pbuf[offset] = 0x41424344;
	offset += 8;
	*(int8_t  *)&pbuf[offset] = 0x45;
	offset += 4;
	*(int16_t *)&pbuf[offset] = 0x4647;
	printf("buf: %s\n", buf);
}

int main(void)
{
	func1();
	return 0;
}
