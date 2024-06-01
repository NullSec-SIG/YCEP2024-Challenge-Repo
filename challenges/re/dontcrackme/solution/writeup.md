# dontcrackme

This challenge was made to appear intimidating, despite its straightforward solution. The choice was made to give players a chance to try using various tools to approach this problem. 

## Solution
1. We have a file `chall` provided
2. Simply running `strings chall | grep YCEP24` will yield the flag

There are other alternative ways to solve this, a notable one being simply attempting the password `P@ssw0rd`, which players can find either by using `strings` or using the following method:
1. Decompile `chall` to C.
2. Search for the function where the password check is done. Provided below is what I got from my decompilation for reference. Note that I removed some useless code inbetween as that was placed in just as a distraction.
```c
__int64 sub_2BE2()
{
  unsigned __int64 *v0; // rax
  __int64 v1; // rbx
  char *v2; // rax
  __int64 v3; // rbx
  __int64 v4; // rax
  const char *v5; // rbx
  __int64 v6; // rax
  const char *v7; // rax
  __int64 v9; // [rsp+50h] [rbp-90h] BYREF
  __int64 v10; // [rsp+58h] [rbp-88h] BYREF
  __int64 v11; // [rsp+60h] [rbp-80h] BYREF
  __int64 v12; // [rsp+68h] [rbp-78h] BYREF
  __int64 v13; // [rsp+70h] [rbp-70h] BYREF
  __int64 v14; // [rsp+78h] [rbp-68h] BYREF
  __m128i v15; // [rsp+80h] [rbp-60h] BYREF
  __m128i v16; // [rsp+90h] [rbp-50h] BYREF
  char v17[40]; // [rsp+A0h] [rbp-40h] BYREF
  unsigned __int64 v18; // [rsp+C8h] [rbp-18h]

  v18 = __readfsqword(0x28u);
  LODWORD(v14) = 256;
  sub_3CE1(&v9, (__int64)&v14);
  sub_3D96(&v10, (__int64)"P@ssw0rd");
  v0 = (unsigned __int64 *)sub_3ED4((__int64)&v9);
  sub_3EF9(&v11, *v0);
  std::allocator<char>::allocator(&v14);
  sub_389A((__int64)v17, "enter password: ", (__int64)&v14);
  sub_36F2((__int64)v17, 50);
  std::string::~string(v17);
  std::allocator<char>::~allocator(&v14);
  v1 = *(_QWORD *)sub_3ED4((__int64)&v9);
  v2 = (char *)sub_3FAC((__int64)&v11);
  std::istream::getline((std::istream *)&std::cin, v2, v1);
  v14 = std::istream::gcount((std::istream *)&std::cin);
  sub_4061(&v12, (__int64)&v14);
  v3 = sub_4114((__int64)&v12);
  v14 = sub_3FAC((__int64)&v11);
  sub_415D(&v13, (__int64)&v14, v3);
  v4 = sub_4250((__int64)&v10);
  v5 = (const char *)std::string::c_str(v4);
  v6 = sub_4250((__int64)&v13);
  v7 = (const char *)std::string::c_str(v6);
  LOBYTE(v5) = strcmp(v7, v5) == 0;
  sub_3E6C((__int64)&v13);
  sub_40AC((__int64)&v12);
  sub_3F50((__int64)&v11);
  sub_3E6C((__int64)&v10);
  sub_3D2E((__int64)&v9);
  return (unsigned int)v5;
}
```
3. If we follow backwards from the `strcmp` call, we can observe that `v5` originates from `v4`, which seems to originate from `v10`, which is where `P@ssw0rd` is loaded into. 
4. With the assumption that `v7` is the user input (what else is there to `strcmp`?), we can use `P@ssw0rd` as the password to successfully retrieve the flag.