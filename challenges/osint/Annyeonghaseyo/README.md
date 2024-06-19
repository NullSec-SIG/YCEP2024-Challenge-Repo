# Annyeonghaseyo

I went to Korea and took a random photo before uploading it to Instagram.
I was then tasked to turn this photo into an OSINT challenge. Find where
the photo was taken and retrieve a tourist map of the location. With reference
to the tourist map, the flag would be the marking that is the closest to the
**pavilion** in the photo, in the format of `YCEP24{number_marking}`. Replace any
spaces with underscores, and ensure that the first letter of each word
is capitalized.

For example, given a map that contains:

1. Visitor Centre
2. Battlestar Galatica
3. Lights, Camera, Action!

And the object in the photo seems to be taken near the Battlestar Galatica, the flag
would be `YCEP24{2_Battlestar_Galatica}`.

## Summary

- **Author:** Bowen
- **Category:** Osint
- **Difficulty:** Medium

## Files

- dist/image.jpg

## Flags

- `YCEP24{11_Pond_Garden}` (static)
- `YCEP24{14_Korean_Garden}` (static)
