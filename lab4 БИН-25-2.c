#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#define COLUMN_WIDTH 30
const char* cyr_to_translit(unsigned char c) {
    static const char* table[] = {
        "a", "b", "v", "g", "d", "e", "yo", "zh", "z", "i", "j", "k", "l", "m", "n", "o",
        "p", "r", "s", "t", "u", "f", "kh", "ts", "ch", "sh", "shch", "", "y", "", "e", "yu", "ya"
    };
    if (c >= 0xE0 && c <= 0xFF) return table[c - 0xE0]; 
    if (c >= 0xC0 && c <= 0xDF) return table[c - 0xC0]; 
    if (c == 0xA8) return "yo";
    if (c == 0xB8) return "yo"; 

    return NULL; 
}

void process_file(const char* filename) {
    FILE* f = fopen(filename, "rb");
    if (!f) {
        perror(filename);
        return;
    }
    printf("--- Processing file: %s ---\n", filename);
    char word[1024];
    char translit_word[2048];
    int word_len = 0;
    int c;
    while ((c = fgetc(f)) != EOF) {
        if (!isspace(c)) {
            if (word_len < 1023) word[word_len++] = (char)c;
        } else {
            if (word_len > 0) {
                word[word_len] = '\0';
                translit_word[0] = '\0';

                int char_count = 0;
                for (int i = 0; i < word_len; i++) {
                    const char* t = cyr_to_translit((unsigned char)word[i]);
                    if (t) {
                        strcat(translit_word, t);
                    } else {
                        char tmp[2] = {word[i], '\0'};
                        strcat(translit_word, tmp);
                    }
                    char_count++;
                }
                printf("%*s | (chars: %d)\n", COLUMN_WIDTH, translit_word, char_count);
                word_len = 0;
            }
            if (c == '\n') printf("\n");
        }
    }
    fclose(f);
}

int main(int argc, char* argv[]) {
    if (argc < 2) {
        printf("Использование: %s <файл1> <файл2> ...\n", argv[0]);
        return 1;
    }
    for (int i = 1; i < argc && i <= 1000; i++) {
        process_file(argv[i]);
    }

    return 0;
}
