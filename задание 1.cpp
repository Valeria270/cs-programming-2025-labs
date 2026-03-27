#include <stdio.h>
#include <math.h>
#include <locale.h>
int main() {
    setlocale(LC_ALL, "Russian");
    double a, b, c;
    double D, x1, x2;
    do{
	    printf("введите коэффициенты уравнения(a, b, c):");
	    if (scanf(" %lf %lf %lf", &a, &b, &c) !=3) {
	    	printf("mistake.\\n");
	    	return 1;
	    }
	    D=pow(b,2)-4*a*c;
	    if (D>=0) {
		    x1=(-b+sqrt(D))/2*a;
		    x2=(-b-sqrt(D))/2*a;
		    printf("x1=%.2f\n", x1);
		    printf("x2=%.2f\n", x2);
		} else {
			printf("The diskriminant is negative. (D=%.2f\n) корней нет.\\n", D);
		}		
	} while (D !=0);  
    return 0;
}
