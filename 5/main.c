#include <stdlib.h>
#include <stdio.h>
//#include "matrix_ops.h"
#include <locale.h>


int** allocate_matrix(int N){
	
	int i;
	int** matrix= (int**)malloc(N * sizeof(int*));
	for ( i=0; i<N; i++)
	    matrix[i] = malloc(N * sizeof(int));
	return matrix; 
}


int** calculate_matrix(int** A, int** B, int N, char C){
	int i,j,k;
	int** R = allocate_matrix(N);	
    for (int i=0; i<N; i++){
    	for (int j=0; j<N; j++){
    		if (C=='+'){
    			R[i] [j] = A[i] [j] + B[i] [j];
			} else if (C == '-'){
				R[i] [j] = A[i][j] - B[i] [j];
			} else if (C =='*'){
				R[i] [j] = 0;
				for (int k=0; k<N; k++);
			        R[i] [j] += A[i] [k] * B[k]	[j];
			}
		}
	}
	return R;
}







void free_matrix(int** matrix, int N) {
	int i;
	for ( i=0; i<N; i++) free(matrix[i]);
	free(matrix);
}

int main(){
	setlocale (LC_ALL, "Russian");
	int N;
	char C;
	printf("¬ведите размер матриц: \n");
	scanf("%d", &N);
	int** A = allocate_matrix(N);
		printf("allocate_matrix a\n");
//		int A[2][2];
	int** B = allocate_matrix(N);	
	printf("allocate_matrix b\n");	
	
	printf("¬ведите элементы первой матрици: \n");
	int i, j, k;
	char c;
	for (i=0; i<N; i++ ){
	    for( j=0; j<N; j++ ){
	printf("qqq b\n");	
	while ((c = getchar()) != '\n');
		printf("A [%d] [%d] =\n",i,j);		    	
			scanf("%d", &A[i][j]);
	printf("A [i] [j] = %d\n",A [i] [j]);				
		}
    } 
	printf("¬ведите элементы второй матрици: \n");
	for (i=0; i<N; i++ ){
	    for( j=0; j<N; j++ ){
			scanf("%d", &B [i] [j]);
	}
    }
    printf("¬ведите математический знак: \n");
    scanf("%c\n", &C);
	int** R= calculate_matrix(A, B, N, C);
	printf("–езультат: \n");
	for(i=0; i<N; i++){
		for(j=0; j<N; j++){
			printf("%.2lf", R[i] [j]);

	}
			printf("\n");
}
			free_matrix(A, N);
			free_matrix(B, N);
			free_matrix(R, N);
    return 0;
}
