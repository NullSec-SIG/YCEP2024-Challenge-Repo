import random
import signal
import sys


signal.signal(signal.SIGALRM, lambda signum, frame:sys.exit(0))

try:
    with open ("flag.txt", "r") as f:
        flag = f.read()
except FileNotFoundError:
    print("File not found.")
    exit()

print("How quick can you quick maths?")

operands = ["+", "-", "*"]

for i in range(1, 1001):
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    op = random.choice(operands)
    
    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    
    signal.alarm(5)
    ans = input(f"{num1} {op} {num2} = ")
    
    signal.alarm(0)
    
    if ans != str(result):
        print("Not wrong, just different")
        break
    
    if i == 10:
        print(f"Very good. Have a lollipop. \nI hope you used automation.\n{flag}")