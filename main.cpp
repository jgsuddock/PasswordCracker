#include <stdio.h>    /* printf */
#include <stdlib.h>   /* abs */
#include <string.h>   /* strlen */
#include <locale>     /* std::locale, std::toupper */



int main(int argc, char const *argv[])
{
    // 
    // Check Input Arguments
    // 
    if(argc != 4) {
        printf("Error Reading Program Arguments.\n");
        exit (EXIT_FAILURE);
    }

    std::locale loc;

    int size = (int)strlen(argv[1]);
    int cipherNum[size];
    int size2 = (int)strlen(argv[2]);
    int keyNum[size];

    // 
    // Print Cipher Text and Key as Numbers
    // 
    printf("Cipher { ");
    for(int i = 0; i < size; i++) {
        cipherNum[i] = std::toupper(argv[1][i],loc);
        printf("%d ",cipherNum[i]);
    }
    printf("}\n\n");

    printf("Key { ");
    for(int i = 0; i < size2; i++) {
        keyNum[i] = std::toupper(argv[2][i],loc);
        printf("%d ",keyNum[i]);
    }
    printf("}\n\n");

    // 
    // Cipher Text Decryption
    // 
    char plainTxt[size];

    int keyIndex = 0;
    printf("Plain Text: ");
    for(int i = 0; i < size; i++) {
        plainTxt[i] = (((cipherNum[i] - 'A') - (keyNum[keyIndex] - 'A') + 26) % 26) + 'A';
        printf("%c",plainTxt[i]);
        keyIndex++;
        if(keyIndex >= size2) {
            keyIndex = 0;
        }
    }
    printf("\n\n");

    return 0;
}