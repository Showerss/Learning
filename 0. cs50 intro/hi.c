#include <stdio.h>
#include <cs50.h>

int main(void)
{
    string words[2];
    words[0] = "hi!";
    words[1] = "bye!";

    printf("%c%c%c\n", words[0][0], words[0][1], words[0][2]);
    printf("%s\n", words[1]);
}