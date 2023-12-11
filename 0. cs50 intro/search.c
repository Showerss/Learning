#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    string strings[] = {"battleship", "boot", "cannon", "iron", "thimble", "tophat"};

    string s = get_string("String: ");

    for (int i = 0; i < 6; i++)
    {
        //if the function from the header strcmp analyzes strings and then opens up the current one we're analyzing and compares it so S and it returns true
        if (strcmp(strings[i], s) == 0 )
        {
            printf("Found!\n");
            return 0;
        }
    }
    printf("Not found!\n");
    return 1;
}