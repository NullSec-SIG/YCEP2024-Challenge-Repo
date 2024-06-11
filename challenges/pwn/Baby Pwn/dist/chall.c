#include <stdio.h>
#include <stdlib.h>
#include <signal.h>

void flag() { // you dont need to know how this function works, just that it gets called when you trigger a segfault, and prints the flag
    char flag[100];
    FILE *f = fopen("flag", "r");
    if (f == NULL) {
        printf("Flag file is missing.\n");
        exit(1);
    }
    fgets(flag, 100, f);
    printf("Woah, how did you get here?\n");
    printf("%s\n", flag);
    fclose(f);
    exit(0);
}

void vuln() { // this is the function that you will be exploiting
    char buf[100];

    signal(SIGSEGV, flag); // SIGSEGV is the signal that is sent when you trigger a segfault, it is set to call the flag function

    printf("Hi there! Enter your name: ");
    gets(buf);
    printf("Hello, %s!\n", buf);
}

int main() { // you also dont need to know how this works
    setvbuf(stdin, 0, 2, 0);
    setvbuf(stdout, 0, 2, 0);
    vuln();
    return 0;
}