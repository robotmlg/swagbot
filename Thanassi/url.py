from urllib2 import *

f = urlopen("http://en.wikipedia.org/wiki/Leonhard_Euler")
s = f.read()
f.close()

s = s.split("Died")
record = False
result = ""
print s[1]
for i in range(len(s[1])):
    if record == True and s[1][i] == '<':
        break
    elif record == True:
        result = result + s[1][i]
    elif s[1][i] == '>' and s[1][i + 1] != '<':
        record = True
print result
