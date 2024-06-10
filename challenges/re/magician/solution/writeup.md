# Magician
elaborated a bit cuz this is kinda troublesome

1. Open the program in GDB
    - Start the program in GDB by running
    ```
    gdb chall
    ```

2. Set a breakpoint at `main`
    - This will help you disassemble `main` with the right addresses since the program has PIE (Position Independent Executable) enabled. This can be done by running the following command:
    ```
    break main
    ```

3. Run the program
    - Start the program in GDB by running
    ```
    run
    ```

4. Disassemble `main`
    - Disassemble `main` to find out where the program is unlinked. Use
    ```
    disassemble main
    ```

5. Search for the `unlink` call
    - Look for the line where `unlink` is called. It might look like the following:
    ```
    0x0000555555557e73 <+3450>:	call   0x555555556360 <unlink@plt>
    ```
    (This might differ for you)

6. Set a breakpoint at the `unlink` call
    - Set a breakpoint at the `unlink` call to pause the program before it deletes itself. You can do so by running
    ```
    break *0x0000555555557e73
    ```
    (Replace the address with the one you have)

7. Disassemble the next few addresses
    - Look at the next few instructions after the current `rip` by using the following command:
    ```
    x/5i $rip
    ```

    - You should get an output that looks like the following:
    ```
    gef➤  x/5i $rip
    =>  0x555555557e73 <main+3450>:	call   0x555555556360 <unlink@plt>
        0x555555557e78 <main+3455>:	mov    edi,0xb
        0x555555557e7d <main+3460>:	call   0x555555556410 <raise@plt>
        0x555555557e82 <main+3465>:	lea    rax,[rbp-0x29c0]
        0x555555557e89 <main+3472>:	mov    rdi,rax
    ```

8. Set the instruction pointer `$rip` to skip the `unlink` and `raise` calls.
    - Set `rip` to the next instruction after those calls. In my case, I would do 
    ```
    set $rip = 0x555555557e82
    ```
    (Your address may differ)

9. Continue the program to retrieve the flag
    - Continue program execution to retrieve the flag
    ```
    continue
    ```

10. Decode flag
    - The flag you receive should be base64 encoded. I will not elaborate on how this is determined, since any CTF player worth their salt should be able to recognise a base64 encoded string when they see one. Decoding the string will yield the flag.