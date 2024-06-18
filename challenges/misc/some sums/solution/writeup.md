# some sums 
This challenge serves as an introduction for participants to learn how to write a simple pwntools script.

Participants could do all 1000 sums manually, which is commendable, but will take a lot of time and effort. 

A timeout of 5 seconds has also been implemented to encourage participants to use a solve script.

## Solution
Possible solve script:
```py
from pwn import *

s = remote('challs.ycep24.nullsecsig.com', 12008)

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
```