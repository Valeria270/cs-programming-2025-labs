#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <stdbool.h>
bool is_vowel(int c) {
    c = tolower(c);
    return (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u');
}
bool is_consonant(int c) {
    return (isalpha(c) && !is_vowel(c));
}
int main() {
    char filename[256];
    FILE *file;
    int c; 
    long total_chars = 0;
    long lines = 0;
    long digits = 0;
    long punct = 0;
    long whitespace = 0;
    long letters = 0;
    long lowercase = 0;
    long uppercase = 0;
    long vowels = 0;
    long consonants = 0;
    printf("Введите имя файла: ");
    if (scanf("%255s", filename) != 1) {
        printf("Ошибка ввода имени файла.\n");
        return 1;
    }
    file = fopen(filename, "r");
    if (file == NULL) {
        perror("Ошибка открытия файла");
        return 1;
    }
    while ((c = fgetc(file)) != EOF) {
        total_chars++;

        if (c == '\n') {
            lines++;
        }
        if (isdigit(c)) {
            digits++;
        }
        if (ispunct(c)) {
            punct++;
        }
        if (isspace(c)) {
            whitespace++;
        }
        if (isalpha(c)) {
            letters++;
            if (islower(c)) {
                lowercase++;
            }
            if (isupper(c)) {
                uppercase++;
            }
            if (is_vowel(c)) {
                vowels++;
            } else if (is_consonant(c)) {
                consonants++;
            }
        }
    }
    fclose(file);
    printf("\n--- Результаты анализа файла ---\n");
    printf("Общее количество символов: %ld\n", total_chars);
    printf("Количество строк: %ld\n", lines + 1); 
    printf("Количество цифр: %ld\n", digits);
    printf("Количество знаков препинания: %ld\n", punct);
    printf("Количество пробельных символов: %ld\n", whitespace);
    printf("Количество букв: %ld\n", letters);
    printf("  из них строчных: %ld\n", lowercase);
    printf("  из них прописных: %ld\n", uppercase);
    printf("Количество гласных букв: %ld\n", vowels);
    printf("Количество согласных букв: %ld\n", consonants);
    return 0;
}
