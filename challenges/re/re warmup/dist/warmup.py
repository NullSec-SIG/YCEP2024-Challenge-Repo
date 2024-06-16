flag = r"YCEP24{w4rmup_15_ezpz}"

encode = []

for char in flag:
    encode.append(chr(ord(char) + 3))
    
message = ''.join(encode)

print(message)

# Output: \FHS57~z7upxsb48bh}s}
