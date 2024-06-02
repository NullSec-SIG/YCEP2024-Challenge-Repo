# fleXOR Solution

1. A ciphertext string is given. At first glance, it seems to be base64 encoded. The challenge title and description hints XOR encryption. However, we are not given the key, and we must try to brute force the key in order to decrypt the ciphertext.

Possible solve script:

```py
import base64

encrypted_b64 = "NzYpPEFRGBxBGx4sVDwNQQIzMTc2WUYzKkM3IF0qNFwhGA==" # Given string
flag_prefix = "YCEP24{" # Flag prefix will aid the decryption algo check & reduce brute force tries

encrypted_bytes = base64.b64decode(encrypted_b64) # Since the given string seems to be base64 encoded, 1st step: decode base64 to get xor encrypted bytes
#print("Encrypted bytes: ", encrypted_bytes)

def xor_decrypt(ct, key): # xor decrypt function for loop below
    '''iterates through ciphertext & xors corresponding ciphertext byte with key byte'''
    decrypted = b''
    for i in range(len(ct)):
        decrypted_byte = ct[i] ^ key[i % len(key)] # rearrange equation: ciphertext = key ^ plaintext
        decrypted += bytes([decrypted_byte])
    return decrypted


for key_length in range(1, len(flag_prefix) + 1): # iterate through flag prefix (format)
    key = bytearray(key_length)
    for i in range(key_length):
        key[i] = encrypted_bytes[i] ^ ord(flag_prefix[i]) 

    decrypted = xor_decrypt(encrypted_bytes, key)
    decrypted_text = decrypted.decode('utf-8', errors='ignore')

    if decrypted_text.startswith(flag_prefix):
        print("Key:", bytes(key))
        print("Decrypted:", decrypted_text)
```

Output:
```
Key: b'nullsec'
Decrypted: YCEP24{r4wr_1_c4n_BRU73_F0RC3_X0R}
```
