#include <stdio.h>    /* printf, fgets */
#include <stdlib.h>   /* atoi */
#include <string.h>   /* strlen */
#include <locale>     /* std::locale, std::toupper */

int main(int argc, char const *argv[])
{
    if(argc != 4) {
        printf("Error Reading Program Arguments.\n");
        exit (EXIT_FAILURE);
    }

    int size = (int)strlen(argv[1]);
    std::locale loc;

    int cipherNum[size];

    printf("{ ");
    for(int i = 0; i < size; i++) {
        cipherNum[i] = std::toupper(argv[1][i],loc);
        printf("%d ",cipherNum[i]);
    }
    printf("}\n\n");

    return 0;
}