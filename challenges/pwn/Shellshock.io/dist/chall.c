// gcc -g -o chall chall.c -fno-stack-protector -z execstack -no-pie

#include <stdio.h>
#include <stdlib.h>

int main() {
    setvbuf(stdin, 0, 2, 0);
    setvbuf(stdout, 0, 2, 0);

    char name[32];

    printf("What's your name?\n> ");
    gets(name);

    printf("Hello, %s", name);

    return 0;
}