# Galvanised Square Steel Solution

1. Unzip file with 7zip
2. Convert qcow2 to img / vmdk with qemu-img tool
3. Look through common directories like the documents folder in the home directory of the ycep24 user. Find that there is a .secret folder. Part 1 of the flag is in the folder.
4. The next part is in .bash_history file.
5. Last part is via password cracking of the `hacker` user in /etc/shadow. $1 shows that it is in MD5, and $$... shows that the password hash is unsalted. Use John the Ripper / HashCat to crack the password, and join the parts together for the full flag.