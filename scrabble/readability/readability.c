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
    printf("%i\n", count_letters(input));
    printf("%i\n", count_words(input));
    printf("%i\n", count_sentences(input));
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

int count_words(string text)
{
    int length = strlen(text);
    int cnt = 0;
    for (int i = 0; i < length; i++)
    {
        if (text[i] == ' ')
            cnt++;
    }
    return cnt+1;
}

int count_sentences(string text)
{
    int length = strlen(text);
    int cnt = 0;
    for (int i = 0; i < length; i++)
    {
        if (text[i] == '.' || text[i] == '?' || text[i] == '!')
            cnt++;
    }
    return cnt;
}