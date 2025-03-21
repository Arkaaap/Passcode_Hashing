/*AUTHOR Arkaaap
IMPLEMENTING CAESAR CIPHER USING C
DATE 3/19/25
*/

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define TRUE 1

void Banner() {
    printf("  #####     #    #######  #####     #    ######      #####  ### ######  #     # ####### ######  \n");
    printf(" #     #   # #   #       #     #   # #   #     #    #     #  #  #     # #     # #       #     # \n");
    printf(" #        #   #  #       #        #   #  #     #    #        #  #     # #     # #       #     # \n");
    printf(" #       #     # #####    #####  #     # ######     #        #  ######  ####### #####   ######  \n");
    printf(" #       ####### #             # ####### #   #      #        #  #       #     # #       #   #   \n");
    printf(" #     # #     # #       #     # #     # #    #     #     #  #  #       #     # #       #    #  \n");
    printf("  #####  #     # #######  #####  #     # #     #     #####  ### #       #     # ####### #     # \n");
}

void Caesar_Cipher (char *c,int key)
{

    int l = strlen (c);
    char *c1 = (char *)malloc(l+1);
    for (int i=0;i<l;i++)
    {
        if (c[i] >= 'A' && c[i] <= 'Z'|| c[i]>='a' && c[i]<='z' && c[i] == " "){
        c1[i] = c[i]+(key%26); // E = (x+key)%26
    }
    else {
        c1[i] = c[i]-26;
    }
}


printf ("%s",c1);
}

void reverse_Cipher (char *c)
{
    int l = strlen(c);
    for (int i=(l-1);i>=0;i--)
    {
        printf ("%c",c[i]);
    }
}


void reverse_Cipher1 (char *c)
{
    int l = strlen(c);
    for (int i=(l-1);i>=0;i--)
    {
        printf ("%c",c[i]-1);
    }

}
    

int main (void)
{
    int n;
    while (TRUE){
    Banner();
    printf ("1.CAESAR_Cipher  :\n");
    printf ("Press 2-3.reverse _Cipher  &  More :\n");
    printf ("4. EXIT\n");
    printf ("Enter The Choice :\n");
    scanf ("%d",&n);
    char c[100];
    int key;
    printf ("\n");

    switch (n)
    {
        case 1:
        printf ("Enter The String :");
        scanf ("%s",c);
        printf ("Enter The Key :");
        scanf ("%d",&key);
        Caesar_Cipher(c,key);
        break;
        case 2:
        printf ("Enter The String :");
        scanf ("%s",c);
        reverse_Cipher(c);
        break;
        case 3:
            printf ("Enter The String :");
            scanf ("%s",c);
            reverse_Cipher1(c);
            break;
        case 4.
            exit (0);
            break;
        default:
            fprintf (stdout,"Invalid Choice !!");
    }


    return (0x0);
}
}
