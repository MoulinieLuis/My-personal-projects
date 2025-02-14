#include <stdio.h>
#include <stdlib.h> 

float calificacionDepartamental(float, float);
float calificacionParcial(float, float);
float tareasTrabajosParticipacion(float, float, float);

int main() {
    float ed1, ed2, ep1, ep2, t, tr, p, pr, calif;

    printf("Este programa calcula la calificacion de un alumno\n\n");
    printf("Ingrese la calificación del primer examen departamental: ");
    scanf("%f", &ed1);
    printf("Ingrese la calificación del segundo examen departamental: ");
    scanf("%f", &ed2);
    printf("Ingrese la calificación del primer examen parcial: ");
    scanf("%f", &ep1);
    printf("Ingrese la calificación del segundo examen parcial: ");
    scanf("%f", &ep2);
    printf("Ingrese la calificación de las tareas: ");
    scanf("%f", &t);
    printf("Ingrese la calificación de los trabajos: ");
    scanf("%f", &tr);
    printf("Ingrese la calificación de las participaciones: ");
    scanf("%f", &p);
    printf("Ingrese la calificación del proyecto: ");
    scanf("%f", &pr);

    calif = calificacionDepartamental(ed1, ed2) +  calificacionParcial(ep1, ep2) +  tareasTrabajosParticipacion(t, tr, p) +  (pr * 0.10);

    printf("La calificación final del alumno es: %.2f\n", calif);

    return 0;
}

float calificacionDepartamental(float ed1, float ed2) {
    return ((ed1 + ed2) / 2) * 0.40;
}

float calificacionParcial(float ep1, float ep2) {
    return ((ep1 + ep2) / 2) * 0.30;
}

float tareasTrabajosParticipacion(float t, float tr, float p) {
    return ((t + tr + p) / 3) * 0.20;
}