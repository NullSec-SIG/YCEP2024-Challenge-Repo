# UPX
1. Unpack challenge binary with `upx -d chall`
2. Open up the unpacked binary in IDA/Ghidra 
3. Find the comparison statement leading to the branch between good/bad path (This would be a `cmp` instruction very close to a `jnz` instruction)
4. Get the constant that the user input is being compared to (`0xDEAD` or `57005` in decimal)
```
mov     [rbp+var_C], 0DEADh
cmp     [rbp+var_C], eax
jnz     short loc_25B0
```
5. Run the binary and input the number
6. Flag will be yielded