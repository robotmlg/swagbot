from urllib2 import *
t1 = "http://en.wikipedia.org/wiki/Leonhard_Euler"
t2 = "http://en.wikipedia.org/wiki/Kurt_Cobain"
t3 = "http://en.wikipedia.org/wiki/Nelson_Mandela"
t4 = "http://en.wikipedia.org/wiki/Leonardo_DaVinci"
t5 = "http://en.wikipedia.org/wiki/Archimedes"
t6 = "http://en.wikipedia.org/wiki/Pythagoras"

def findTheDeath(url):
    f = urlopen(url)
    s = f.read()
    f.close()
    for i in range(len(s)):
        if s[i] == 'D' and s[i+1] == 'a' and s[i+2] == 't' and s[i+3] == 'e' and s[i+4] == ' ' and s[i+5] == 'o' and s[i+6] == 'f' and s[i+7] == ' 'and s[i+8] == 'd':
            record = False
            result = ""
            for j in range(i+18, len(s)):
                if record == True and s[j] == '<':
                    return result
                elif record == True:
                    result += s[j]
                elif s[j] == '>' and s[j+1] != '<' and s[j+3] != '<':
                    record = True

#print findTheDeath(t6)

def findTheBirth(url):
    f = urlopen(url)
    s = f.read()
    f.close()
    for i in range(len(s)):
        if s[i] == 'D' and s[i+1] == 'a' and s[i+2] == 't' and s[i+3] == 'e' and s[i+4] == ' ' and s[i+5] == 'o' and s[i+6] == 'f' and s[i+7] == ' 'and s[i+8] == 'b':
            record = False
            result = ""
            for j in range(i+18, len(s)):
                if record == True and s[j] == '<':
                    return result
                elif record == True:
                    result += s[j]
                elif s[j] == '>' and s[j+1] != '<' and s[j+3] != '<':
                    record = True

#print findTheBirth(t1)
