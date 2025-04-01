#include <stdio.h>

int main(){

int num = 1;
printf("%d", num);
/*This shows the actual number*/

printf("%d", num++);
/*This increments the value and prints it after*/

printf("%d", ++num);
/*This increments the number before showing it*/

getchar();
return 0;
}