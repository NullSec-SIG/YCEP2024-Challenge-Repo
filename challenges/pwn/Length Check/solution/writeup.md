# Length Check

The solution to this involves an integer overflow to abuse the numbers
of characters read. We see that even though there is a check to see if
the `length` variable is smaller than `21`, we convert it to an unsigned
int before calling `read`, which effectively allows negative inputs to
overflow into positive inputs.

```c
if (length > 21) {
    puts("Length is too large.");
    return 1;
}

read(0, input, (unsigned int) length);
```

Thus, the solution to this challenge is to simply specify your input
length as a negative value such as `-1`, and you are free to input
a string that is up to a few million characters long.
