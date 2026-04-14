#include <stdio.h>
#include <math.h>
#include <locale.h>
#include "TRIANG.h"
#include <stdbool.h>

int main() {
	setlocale (LC_ALL, "Russian");
	double a, b, c;
	printf("Введите длины сторон треугольника: \n");
	if (scanf("%lf %lf %lf" , &a, &b, &c) !=3) {
	    printf("Ошибка ввода \n");
	    return 1;
	}
	if (isValidTriangle (a, b,c)) {
		printf ("Периметр: %.2f\n", calculatePerimeter (a, b, c));
		printf ("Площадь: %.2f\n", calculateArea (a, b, c));
	} 
	else {
		printf("Треугольника не существует: \n");
	}
	return 0;
}
    
    

