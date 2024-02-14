#include <stdio.h>

int num_max(int value1, int value2) {
    return (value1 > value2) ? value1 : value2;
}

int main() {
    int numero1 = 342, numero2 = 392;

    printf("%d,%d\n", numero1, numero2);
    
    int resultado = num_max(numero1, numero2);

    printf("O valor máximo é: %d\n", resultado);

    return 0;
}
