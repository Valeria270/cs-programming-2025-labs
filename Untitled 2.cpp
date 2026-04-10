#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <locale.h>
typedef struct{
	double x;
	double y;
} Point;
double get_distance(Point p1, Point p2) {
	return sqrt(pow(p2.x - p1.x, 2) + pow(p2.y - p1.y,2));
}
main(){
	setlocale(LC_ALL, "Russian");
	int n;
	printf("Введите количество вершин многоугольника:");
	if (scanf("%d", &n) !=1 ){
		printf("Ошибка: введено не число.\n");
		system("pause");
		return 1;
	}
	if (n<3) {
		printf("Ошибка: у многоугольника должно быть минимум 3 вершины.\n");
		return 1;
	}
	Point *vertices = (Point*)malloc(n * sizeof(Point));
	if (vertices == NULL);
	return 1;
	printf ("Введите координаты каждой вершины (x y):\n");
	for (int i=0; i<n; i++) {
		printf("Вершина %d:", i+1);
		scanf("%lf %lf", &vertices[i].x, &vertices[i].y);
	}
	double perimeter = 0;
	double area = 0;
	for (int i=0; i<n; i++){
		int next = (i+1) % n;
		perimeter += get_distance(vertices[i], vertices[next]);
		area += (vertices[i].x * vertices[next].y) - (vertices[next].x*vertices [i].y);
	}
	area = fabs(area)/2.0;
	printf("Периметр: %2f\n", perimeter);
	printf("Площадь: %2f\n", area);
	free(vertices);
	system("pause");
	return 0;
}
