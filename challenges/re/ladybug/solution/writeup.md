# Lad(y)ebug
1. Open the binary in IDA/Ghidra
2. Set a breakpoint on the `test` instruction after the call to `IsDebuggerPresent`. The `test` instruction will set the `Zero Flag (ZF)` if `RAX` is `0`, which will allow the `jz (Jump if Zero)` instruction to bring us to the branch where the flag is output.
3. When breakpoint is reached, set `RAX` to `0`.
4. Find flag in debug console.