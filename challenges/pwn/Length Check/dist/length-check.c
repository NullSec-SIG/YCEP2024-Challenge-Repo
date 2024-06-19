#include <stdio.h>
#include <string.h>
#include <unistd.h>

void show_flag() {
    puts("YCEP24{f4k3_flag_f0r_t3st1ng}");
    return;
}

int main() {
    setvbuf(stdin, 0, 2, 0);
    setvbuf(stdout, 0, 2, 0);
    setvbuf(stderr, 0, 2, 0);

    char input[21];
    int length;

    puts("Welcome to the length checker!");
    puts("We check the length of your input :D");

    printf("Enter the length of your input: ");
    scanf("%d", &length);
    getchar();

    if (length > 21) {
        puts("Length is too large.");
        return 1;
    }

    printf("Enter your input: ");
    read(0, input, (unsigned int) length);

    length = strlen(input);

    printf("The length of your input is: %d\n", length);

    if (strlen(input) > 21) {
        puts("Congrats!");
        show_flag();
    }

    return 0;
}
