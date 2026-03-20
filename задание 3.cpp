#include <stdio.h>
#include <string.h>
#include <locale.h>
int main() {
	setlocale (LC_ALL, "Russian");
	char str[81];
	printf("¬ведите символы: \n");
	if (fgets(str, sizeof(str), stdin) ==NULL) {
		printf("ошибка ввода \n");
    	return 1;
    }
	for (int i=0; str[i] != '\0'; ++i) { 
	    if (str [i] =='a') {
	    	str [i] =='A';
		}
	    else if (str [i] =='b') {
	     	str[i] ='B';
		 }	
	}
	printf("–езультат: %s", str);
	return 0;
}
	
