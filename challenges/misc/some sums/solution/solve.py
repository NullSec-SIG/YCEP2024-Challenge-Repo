from pwn import *

s = remote("challs.ycep24.nullsecsig.com", 9118)

header = s.recvline()

def solve(n1, op, n2):
	n1 = int(n1)
	n2 = int(n2)
	
	if op == b"+":
		return n1 + n2
	elif op == b"-":
		return n1 - n2
	elif op == b"*":
		return n1 * n2
	else:
		return None
		
while True:

	prompt = s.recv()
	print(prompt)
	
	if b"=" not in prompt:
		break
	else:
		eqn = prompt.split(b" ")
		n1, op, n2 = eqn[0], eqn[1], eqn[2]
		print(b"n1:" + n1 + b" op:" + op + b" n2:" + n2)
		
		result = solve(n1, op, n2)
		print(result)
		
		if result != None:
			s.sendline(str(result))

s.recvall()	
s.close()