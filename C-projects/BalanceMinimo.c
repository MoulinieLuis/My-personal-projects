/*Leer el peso en gramos (máximo 5000) y determinar el menor número de pesas que hay que poner en una balanza
(con pesos: 1 g, 2 g, 5 g, 10 g, 50 g, 100 g, 200 g, 500 g, 1000 g) para equilibrar un determinado peso en gramos, introducida por teclado.

*/

#include <stdio.h>
#include <stdlib.h>
#define gramos 5000

void pesasMinimas(int g);


int main(){

int g = 0;

printf("Ingresa un número de gramos: ");
scanf("%d", &g);


printf("El menor número de pesas considerando pesos de 1, 2, 5, 10, 50, 100, 200, 500 y 1000 gramos, para equilibrar %d gramos son: \n\n", g);
pesasMinimas(g);

getchar();
return 0;
}


void pesasMinimas(int g){

int aPesas[8] = {0};
int r=g;


do{
    if(r >= 1000){
        r = g - 1000;
        aPesas[0]++;
    } else if (r >= 500){
        r = g - 500;
        aPesas[1]++;
        
    } else if (r >= 200){
        r = g - 200;
        aPesas[2]++;
        
    } else if (r >= 100){
        r = g - 100;
        aPesas[3]++;
        
    } else if (r >= 50){
        r = g - 50;
        aPesas[4]++;
        
    } else if (r >= 10){
        r = g - 10;
        aPesas[5]++;
        
    } else if (r >= 5){
        r = g - 5;
        aPesas[6]++;
        
    } else if (r >= 2){
        r = g - 2;
        aPesas[7]++;
        
    } else if (r >= 1){
        r = g - 1;
        aPesas[8]++;
    }

} while(r > 0);


printf("%d pesas de 1,000 gramos\n", aPesas[0]);
printf("%d pesas de 500 gramos\n", aPesas[1]);
printf("%d pesas de 200 gramos\n", aPesas[2]);
printf("%d pesas de 100 gramos\n", aPesas[3]);
printf("%d pesas de 50 gramos\n", aPesas[4]);
printf("%d pesas de 10 gramos\n", aPesas[5]);
printf("%d pesas de 5 gramos\n", aPesas[6]);
printf("%d pesas de 2 gramos\n", aPesas[7]);
printf("%d pesas de 1 gramo", aPesas[8]);

}