#include <stdio.h>

void spout_brainrot() {
    asm volatile ("pop %%rax\n\t" "ret" ::: "rax");
}

int main() {
    setvbuf(stdin, 0, 2, 0);
    setvbuf(stdout, 0, 2, 0);
    setvbuf(stderr, 0, 2, 0);

    char brainrot[64];

    puts("Skibidi rizz. Gyatt damn. Uhm what the sigma?");
    printf("/bin/sh\x00");
    printf(" > ");
    
    // read(0, brainrot, 0x64);
    register int syscall_no asm("rax") = 0;
    register int arg1       asm("rdi") = 0;
    register char* arg2     asm("rsi") = brainrot;
    register int arg3       asm("rdx") = 420;
    asm("syscall");

    return 0;
}
