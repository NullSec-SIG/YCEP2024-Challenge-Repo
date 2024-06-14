def scramble(flag):
    char_list = list(flag)
    for i in range(0, len(char_list)):
        if i % 2 != 0:
            templetter = char_list[i]
            templetter2 = char_list[i-1]
            char_list[i] = templetter2
            char_list[i-1] = templetter

    char_list = ''.join(char_list)
    print(char_list)

#scrambled flag
print("CYPE421{l_o00oevs_rcm41bd33_gg_5_n4mngl041m_1mkl}")

