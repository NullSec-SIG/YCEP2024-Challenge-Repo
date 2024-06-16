encoded_message = r"\FHS57~z7upxsb48bh}s}"

decode = []

for char in encoded_message:
    decode.append(chr(ord(char) - 3))
    
flag = ''.join(decode)

print(flag)