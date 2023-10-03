#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>
#include <math.h>

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

int main(void)
{
    string input = get_string("Text: ");
    int letters = count_letters(input);
    int words = count_words(input);
    int sentences = count_sentences(input);
    float lw = letters / words * 100.0;
    float sw = sentences / words * 100.0;
    float result = 0.0588 * lw - 0.296 * sw - 15.8;
    int grade = round(result);
    if (grade >= 16)
        printf("Grade 16+\n");
    else if (grade < 1)
        printf("Before Grade 1\n");
    else
        printf("Grade %i\n", grade);
    return 0;
}

int count_letters(string text)
{
    int length = strlen(text);
    int cnt = 0;
    for (int i = 0; i < length; i++)
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
    return cnt + 1;
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