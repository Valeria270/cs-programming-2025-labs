#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <locale.h>
int main() {
    int n;
    int *P;
    int i, j, p;
	setlocale(LC_ALL, "Russian");
    printf("Введите число n: ");
    if (scanf("%d", &n) != 1) {
        printf("Ошибка ввода.\n");
        return 1;
    }
    if (n < 2) {
        printf("Простых чисел нет.\n");
        return 0;
    }
    P = (int *)malloc((n + 1) * sizeof(int));
    if (P == NULL) {
        printf("Ошибка выделения памяти.\n");
        return 1;
    }
    for (i = 0; i <= n; i++) {
        P[i] = 1;
    }
    p = 2;
    while (p * p <= n) {
        if (P[p] != 0) {
            for (j = p * p; j <= n; j += p) {
                P[j] = 0; 
            }
        }
        do {
            p++;
        } while (p <= n && P[p] == 0);
        if (p > n) break;
    }
    printf("Простые числа до %d:\n", n);
    for (i = 2; i <= n; i++) {
        if (P[i] != 0) {
            printf("%d ", i);
        }
    }
    printf("\n");
    free(P);

    return 0;
}
