#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

int main(void)
{
    string input = get_string("Text: ");
    printf("%i", count_letters(input));
    return 0;
}

int count_letters(string text)
{
    int length = strlen(text);
    int cnt = 0;
    for (int i = 0; i <length; i++)
    {
        if (isalpha(text[i]))
            cnt++;
    }
    return cnt;
}