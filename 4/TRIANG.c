#include <stdbool.h>

	bool isValidTriangle(double a, double b, double c ) {
		return (a+b>c) && (a+c>b) && (b+c>a);
    }
	double calculatePerimeter (double a, double b, double c ){
		return (a+b+c);
	}
	double calculateArea (double a, double b, double c ){
		double p=(a+b+c)/2;
		return sqrt(p * (p-a) * (p-b) * (p-c));	
	} 

