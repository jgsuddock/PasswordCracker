#include <stdio.h>    /* printf, fgets */
#include <stdlib.h>   /* atoi */

int main(int argc, char const *argv[])
{
	char char2num[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

	int i;
	char buffer[256];
	printf ("Enter a number: ");
	fgets (buffer, 256, stdin);
	i = atoi (buffer);
    printf ("The value entered is %d. Its double is %d.\n",i,i*2);


	return 0;
}