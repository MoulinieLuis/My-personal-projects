/*
	Programa que transforma pulgadas a centimetros
	Luis Moulinie
	07 / 02 / 2025
*/

#include <stdio.h>
#include <stdlib.h>

int main(){
	float cm;
	int pulg;
	
	printf("Conversor de pulgadas a cent%cmetros \n", 161);
	printf("Ingresa un n%cmero pulgadas: ", 163);
	scanf("%d", &pulg);
	cm = pulg * 2.54;
	printf ("%d pulgadas = %7.3f cent%Cmetros\n", pulg, cm, 161);
	
	getchar();
	return 0;
}
