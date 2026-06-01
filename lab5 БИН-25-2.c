#include <stdio.h>
int main() {
    int n;
    long long l;
    if (scanf("%d %lld", &n, &l) != 2) return 0;
    for (int i = 0; i < n - 1; i++) {
        int temp;
        scanf("%d", &temp);
    }
    long long total_length = 0;
    for (int i = 0; i < n - 1; i++) {
        long long b_i;
        scanf("%lld", &b_i);
        total_length += b_i;
    }
    printf("%lld\n", total_length / l);

    return 0;
}
