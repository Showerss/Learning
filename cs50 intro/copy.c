for (int i=0, n=strlen(s+1); i < n; i++) // this is better, it calls the function only once
for (int i=0; i < strlen(s); i++) // this is slightly worse it calls the strlen function every time it checks if i is less than strlen(s)

strcpy(t, s);

nul is \0 // this is a character
null is a pointer to address 0x0 in memory

if (s == NULL)
{
    return 1;
}

if (t == NULL)
{
    return 1;
}

// above.. t hese are edge case safey measures,

it is a rule within C that if you use malloc, you must free that variable when it's done being used

