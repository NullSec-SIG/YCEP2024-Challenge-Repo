# Challenge Solution
1. Access https://docs.google.com/spreadsheets/d/1JmmdBPO_h_IPd2XOi8wM7nxEhIylgsOxNDdPWlYlu7o/edit?gid=0#gid=0, you might see a certain message
2. If you decode it, you should get
![Alt text](/images/1.png)
3. That tells you that there is a hidden sheet
4. Create a copy of the sheet to view the hidden sheet
5. You will see another message at the first cell, try decoding it, you will get the following
![Alt text](/images/2.png)
6. This should let you know that it is using MSB, so by sorting the entire range and taking the left most bit of each byte, by using the formula =LEFT(C4,1) and drag it down the whole way. it should look something like this
![Alt text](/images/3.png)
7. Copy paste all of it (010110010100001101000101010100000011001000110100011110110100011100110000001100000100011101001100001100110101111101001101001101000011010101010100001100110101001001111101) into cyberchef and you will get the output 
![Alt text](/images/4.png)

## Flag
`YCEP24{G00GL3_M45T3R}`