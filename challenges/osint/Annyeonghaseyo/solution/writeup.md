# Annyeonghaseyo

This OSINT challenge requires 2 steps to solve. Firstly, one
has to obtain the location of the image, which can be done
through Google's reverse image search. Next, they have to pull
up the tourist map of that place and find the closest
attraction that looks like a pavilion.

## Solution

### 1. Google Image Reverse Search

The first result that is returned reveals that the location of
the photo is in the `Garden of the Morning Calm` in Gapyeong,
Seoul, Korea.

### 2. Obtaining the Tourist Map

When you search for tourist maps for Garden of the Morning Calm,
there are multiple versions of it. We can look through the top
results and look for possible places within the garden in which
the picture may have been taken.

![map](map.png)

As the map only shows the presence of a singular pond, and the
pavilion resides on a body of water, it is logical to conclude
that the photo is taken at number `14`, the Korean Garden.

Thus, we can obtain the flag `YCEP24{14_Korean_Garden}`.

---

## Side Note

Other versions of the map show that the pond is numbered `11`,
the Pond Garden. I have also accounted for this and another
accepted flag is `YCEP24{11_Pond_Garden}`. Hopefully I have not
missed out anything else.
