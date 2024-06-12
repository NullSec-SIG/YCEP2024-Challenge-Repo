# Yumminess

---

## Solution

1. Either by reading the challenge description or the hint, we can infer that the flag is encoded using the [Periodic Table Cipher](https://www.dcode.fr/periodic-table-cipher).
2. Then we decode the output using the [Bacon Cipher](https://www.dcode.fr/bacon-cipher) to get the flag.

---

Original String: `AAAA 56 AAAAAAA 56 A 5 5 56 A 5 56 56 56 AA 56 A 56 AAA 56 AA 5 5 56 A 56 AA 5 56 AA 56 AA 56 A 56 56 A 5 5 56 AA 5 5 56 AAA 5 5 56 AA 56 5 5 56 AA 56 56 AA 5 56 AA 5 56 AA 56 AAA 5 56 56 A 56 A 56 A 56 56 A 56`
Decoded String (Periodic Table) : `AAAABAAAAAAAABAABBBAABBABABAAABAABAAAABAAABBBAABAAABBAAABAAABAABABAABBBAAABBBAAAABBBAAABABBBAAABABAAABBAAABBAAABAAAABBABAABAABAABABAABA`
Decoded String (Bacon) : `BACONISCHEMISTRYOFYUMMINESS`

---

Flag: `YCEP24{BACON_IS_CHEMISTRY_OF_YUMMINESS}`
