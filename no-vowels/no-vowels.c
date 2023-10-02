// Write a function to replace vowels with numbers
// Get practice with strings
// Get practice with command line
// Get practice with switch

#include <cs50.h>
#include <stdio.h>
#include <string.h>

string replace(string s)
{
    for (int i = 0, n = strlen(s); i < n; i++)
    {
        if (s[i] == 'a')
            s[i] = '6';
        if (s[i] == 'e')
            s[i] = '3';
        if (s[i] == 'i')
            s[i] = '1';
        if (s[i] == 'o')
            s[i] = '0';
    }

    return s;
}

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./no-vowels word");
        return 1;
    }
    printf("%s", replace(argv[1]));
    return 0;
}
