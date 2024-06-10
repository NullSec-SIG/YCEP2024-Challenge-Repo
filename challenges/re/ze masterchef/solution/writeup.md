# ze masterchef

The given Python function scrambles the flag by swapping all the even and odd characters. Players are given the scrambled flag after it has been scrambled with the function.

## Solution
just make a function that does the opposite i.e. swaps all the characters back to their original places (they could also solve it on paper if they figure out how it works but i made the flag kinda long)

def reverse_scramble(scrambled_flag):
    char_list = list(scrambled_flag)
    for i in range(1, len(char_list)):
        if i % 2 != 0:
            templetter = char_list[i]
            templetter2 = char_list[i-1]
            char_list[i] = templetter2
            char_list[i-1] = templetter
    print(''.join(char_list))


scrambled_flag = "CYPE421{l_o00oevs_rcm41bd33_gg_5_n4mngl041m_1mkl}"
reverse_scramble(scrambled_flag)







