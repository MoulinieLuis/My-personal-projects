/*
This program draws a square with asterisks based on the user input
Author: Moulinie Ruíz Luis Enrique
Date: 2023-10-05
*/

#include <stdio.h>
#include <stdlib.h>

int main(){

int v, cont1, cont2, cont3;

printf("Type a value: ");
scanf("%d", &v);

printf("\n\n");


/*Prints the upper row*/
for(cont1 = 0; cont1 < v; cont1++){
        printf("*");
}

printf("\n");

/*Prints the body*/
for(cont2 = 0; cont2 < (v - 2); cont2++){
        printf("*");

    for(cont3 = 0; cont3 < (v - 2); cont3++){
        printf(" ");
    }
      printf("*");
      printf("\n");
}


/*Prints the lower row*/
for(cont1 = 0; cont1 < v; cont1++){
        printf("*");
}


getchar();
return 0;
}