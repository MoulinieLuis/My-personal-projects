#include <stdio.h>
#include <string.h>
#include <ctype.h>

int luhn_check(const char *card_number);


int main() {
    char card_number[20];

    printf("Ingrese el número de tarjeta: ");
    scanf("%19s", card_number);

    if (luhn_check(card_number)) {
        printf("Número de tarjeta VALIDO\n");
    } else {
        printf("Número de tarjeta INVALIDO\n");
    }

    return 0;
}


int luhn_check(const char *card_number) {
    int len = strlen(card_number);
    int sum = 0, double_digit;
    int is_second = 0;  // 0 para el primer dígito desde la derecha
    int i; //Declaramos i aquí

    for (i = len - 1; i >= 0; i--) {
        if (!isdigit(card_number[i])) return 0;  // Validación: solo dígitos

        int digit = card_number[i] - '0';

        if (is_second) {
            double_digit = digit * 2;
            if (double_digit > 9)
                double_digit -= 9;
            sum += double_digit;
        } else {
            sum += digit;
        }
        is_second = !is_second;
    }

    return (sum % 10 == 0);
}