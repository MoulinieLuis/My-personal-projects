#include <stdio.h>

int main(){

int num, sum = 0;

while(sum < 10){
printf("Ingrese un n%cmero entre 1 y 2", 163);
scanf("%d", &num);
    
    if(num < 1 || num > 2)
        printf("Error, ingrese un n%cmero v%clido", 163, 161);
    else 
        sum += num;
    }

getchar();
return 0;
}