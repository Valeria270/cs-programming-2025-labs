#include <stdlib.h>
//#include "matricx_ops.h"
double** calculate_matrixq(double** A, double** B, int N, char C){
	int k;
    double** R=(double**)malloc(N * sizeof(double));
    for (int i=0; i<N; i++){
    	R[i]= (double*)malloc(N * sizeof(double));
    }
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
