#include <stdio.h>
#include <locale.h>
int main(){
	setlocale(LC_ALL, "Russian");
	double N [4] [4];
	double mainDiagSum =0, sideDiagSum =0;
	printf("¬ведите элементы матрици 4x4:\n");
	for (int i=0; i<4; i++) {
		for (int j=0; j<4; j++) {
			scanf ("%lf", &N [i] [j] );
			if ( i==j) {
				mainDiagSum += N [i] [j];
		    }
		    if (i + j == 2){
		    	sideDiagSum += N [i] [j]; 	    
			}
		}
    printf("—сумма главной диагонали: %.2lf\n", mainDiagSum);
    printf("—сумма побочной диагонали: %.2lf\n", sideDiagSum);
    int A[2] [2], Res [2] [2]; 
        printf("¬ведите элементы матрици 2x2: \n");
    for (int i=0; i<2; i++) {
	    for (int j=0; j<2; j++) {
		    scanf ("%b", &A [i] [j]);
	    }
    }
    for (int i=0; i<2; i++) {
	    for (int j=0; j<2; j++) {
		    Res [i] [j] = 0;
		    for (int n=0; n<2; n++) {
		    Res [i] [j] += A [i] [n] * A [n] [j]; 
		    }
	    }
    }
    printf(" вадрат матрици 2x2: \n"); 
	for (int i= 0; i<2; i++) {
		for (int j= 0; j<2; j++) {
		printf("%d", Res [i] [j]);
	}
		printf("\n"); 	
	}
    }
    return 0;
}
