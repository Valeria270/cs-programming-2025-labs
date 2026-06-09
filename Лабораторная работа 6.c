#include <stdio.h>
#include <stdlib.h>
#include <math.h>
typedef struct point {
    double x;
    double y;
    int num;
} POINT;
int comparePoints(const void *a, const void *b) {
    POINT *p1 = (POINT *)a;
    POINT *p2 = (POINT *)b;
    if (p1->x < p2->x) return -1;
    if (p1->x > p2->x) return 1;
    if (p1->y < p2->y) return -1;
    if (p1->y > p2->y) return 1;
    return 0;
}
double getSide(POINT a, POINT b, POINT p) {
    return (p.y - a.y) * (b.x - a.x) - (b.y - a.y) * (p.x - a.x);
}
double lineDist(POINT a, POINT b, POINT p) {
    return fabs((p.y - a.y) * (b.x - a.x) - (b.y - a.y) * (p.x - a.x));
}

void findHull(POINT *pts, int n, POINT p1, POINT p2, int side, FILE *out, int *hullIndices, int *hullSize) {
    int ind = -1;
    double max_dist = 0;
    for (int i = 0; i < n; i++) {
        double current_side = getSide(p1, p2, pts[i]);
        if (side == 1 && current_side > 0) { 
            double d = lineDist(p1, p2, pts[i]);
            if (d > max_dist) {
                max_dist = d;
                ind = i;
            }
        } else if (side == -1 && current_side < 0) { 
            double d = lineDist(p1, p2, pts[i]);
            if (d > max_dist) {
                max_dist = d;
                ind = i;
            }
        }
    }
    if (ind == -1) {
        hullIndices[(*hullSize)++] = p2.num;
        return;
    }
    if (side == 1) {
        findHull(pts, n, p1, pts[ind], 1, out, hullIndices, hullSize);
        findHull(pts, n, pts[ind], p2, 1, out, hullIndices, hullSize);
    } else { 
        findHull(pts, n, p1, pts[ind], -1, out, hullIndices, hullSize);
        findHull(pts, n, pts[ind], p2, -1, out, hullIndices, hullSize);
    }
}
int main() {
    FILE *in = fopen("IN.txt", "r");
    if (!in) {
        printf("Ошибка открытия файла IN.txt\n");
        return 1;
    }

    int count = 0;
    POINT temp;
    while (fscanf(in, "%d %lf %lf", &temp.num, &temp.x, &temp.y) == 3) count++;
    rewind(in);

    POINT *points = malloc(count * sizeof(POINT));
    for (int i = 0; i < count; i++) {
        fscanf(in, "%d %lf %lf", &points[i].num, &points[i].x, &points[i].y);
    }
    fclose(in);

    if (count < 3) {
        printf("Недостаточно точек для оболочки.\n");
        return 0;
    }
    qsort(points, count, sizeof(POINT), comparePoints);

    int *hullIndices = malloc(2 * count * sizeof(int));
    int hullSize = 0;
    POINT min_x = points[0];
    POINT max_x = points[count - 1];
    hullIndices[hullSize++] = min_x.num;
    findHull(points, count, min_x, max_x, 1, NULL, hullIndices, &hullSize);
    findHull(points, count, max_x, min_x, 1, NULL, hullIndices, &hullSize);
    FILE *out = fopen("OUT.txt", "w");
    for (int i = 0; i < hullSize; i++) {
        fprintf(out, "%d ", hullIndices[i]);
    }
    fclose(out);
    printf("Результат в файле OUT.txt\n");
    free(points);
    free(hullIndices);
    return 0;
}
