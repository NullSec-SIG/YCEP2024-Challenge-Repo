# Snakes

This challenge is just a basic one on following disassembled Python code.

## Solution
Follow the code to re-construct the flag. The code simply stores `YCEP24` in a variable `flag` and appends characters to it one at a time to reconstruct the flag `YCEP24{SN4KES_4RE_N0T_SC4RY}`. 

Key observations:
1. The `LOAD_CONST (x)` instruction loads a constant value `x` onto the stack.
2. The `STORE_NAME (flag)` instruction stores the value into the variable `flag`.
3. The `BINARY_OP (+=)` instruction appends the loaded constant to the `flag` variable.


The challenge should not take more than a few minutes for players to manually reconstruct the flag by tracing it in a linear manner. 