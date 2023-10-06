#include<stdio.h>
#include<math.h>
#include<string.h>
#include<cs50.h>

int atoi(string c);

int main()
{
	string c = get_string("Nhap vao xau: ");
	printf("%d", atoi(c));
}

int atoi(string c)
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