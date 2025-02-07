/*
	Programa en el que se ingresa un número en segundos y se muestra el resultado en horas, minutos y segundos
	Luis Moulinie
*/

#include <stdio.h>
#include <stdlib.h>

int main(){
	
	int h,m,s;
	
	printf("Ingresa un n%cmero de segundos: ", 163);
	scanf("%i",&s);
	printf("Son: ");
	
	if(s<0) printf("error de datos\a");
	else
	{
		if(s>3600)
		{
			h = s/3600; printf("%i:", h);
			s = s-3600*h;
		}
		if(s>60)
		{
			m=s/60; printf("%i:", m);
			s=s-m*60;
		} else {
			printf("00:");
		}
		if(s>0){
			printf("%i", s);
		} else {
			printf("00");
		}
	}
	
	getch();
	return 0;
}