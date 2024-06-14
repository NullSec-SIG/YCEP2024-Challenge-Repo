# Challenge Solution
0 = base32 cipher<br>
1 = base64 cipher<br>
0101 indicates that the 1st and 3rd part of the flag is decoded using base32, 2nd and 4th part of the flag is decoded using base64.

| Part | Cipher | Encoded | Decoded  |
| --- | --- | --- | --- |
| 1st | Base32 | LFBUKUBSGR5VI=== | YCEP24{T |
| 2nd | Base64 | aElzX0lzTg== | hIs_IsN |
| 3rd | Base32 | E5KF6VRTKJ4Q==== | 'T_V3Ry |
| 4th | Base64 | X0JBNTNEfQ== | _BA53D} |

Join all 4 parts and it should be:

`YCEP24{ThIs_IsN'T_V3Ry_BA53D}`