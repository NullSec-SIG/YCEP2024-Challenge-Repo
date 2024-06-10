# Moonwalk Solution

1. We are given an image file `moonwalk.jpg`. Running `binwalk` reveals a hidden zip file appended at the back of the image:
![binwalk](images/moonwalk1.png)

2. Use the `-e` flag to extract the zip archive:
![binwalk-e](images/binwalk-e.png)

3. cd into the extracted directory shows a file `flag.txt`; viewing the file gives the flag:
![soln](images/soln.png)