/* This program prints a square of asterisks with the size specified by the user
 Author: Mouinie Ruíz ui Enrique
 Date: 2023-10-05
*/

#include <stdio.h>
#include <stdlib.h>

int main(){

int v, cont1, cont2;

printf("Type a value: ");
scanf("%d", &v);

printf("/n/n");

for(cont1 = 0; cont1 < v; cont1++){

    for(cont2 = 0; cont2 < v; cont2++){
        printf("*");
    }
   printf("/n");
}

getchar();
return 0;
}