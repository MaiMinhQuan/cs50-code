#include<stdio.h>
#include<math.h>
#include<string.h>

int atoi(char c[]);

int main()
{
	char c[100];
	gets(c);
	printf("%d", atoi(c));
}

int atoi(char c[])
{
	int len = strlen(c);
	int tmp = c[len - 1] - '0';
	if (len == 0)
		return tmp;
	else
	{
		c[len - 1] = '\0';
		return atoi(c) * 10 + tmp;
	}
}