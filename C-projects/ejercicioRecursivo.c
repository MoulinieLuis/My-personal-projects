/*En este programa trabajo con un ejemplo muy básico de recursión realizando una multiplicación por dos a cada número par de un arreglo ya ingresado*/

#include <stdio.h>

//Prototipos
int SumatoriaPares(int limiteSuperior, int n, int res);
//Los prototipos son la declaración de los módulos que se van a usar después, funcionan para indicarle al preprocesador de C con lo que trabajará después precargando algunos valores

int main() {
    printf("%d", SumatoriaPares(5, 1, 0));
    //La función printf llama al módulo SumatoriaPares
    
    getchar(); //Funciona como un limpiador del buffer de entrada y evita lectura de datos no necesarios como enters
    return 0;
}


int SumatoriaPares(int limiteSuperior, int n, int res) { //En este caso la función de sumatoria crea a las variables limite, n y res dentro de la firma
    if (n > limiteSuperior) //Esta condicional previene que el ciclo sea infinito comparando el elemento n y el límite
        return res; //Regresa el valor resultante
    
    if (n % 2 == 0) //La firma compara si el resultado es par 
        res += n * 2; //Si el valor es par se multiplica por dos y se suma a la variable res
    
    return SumatoriaPares(limiteSuperior, n + 1, res); //Return<función> significa que el módulo es recursivo por lo que todos los números del arreglos sin ser mayores al límite pasaran por el módulo
}