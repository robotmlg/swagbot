from urllib2 import *
t1 = "http://en.wikipedia.org/wiki/Leonhard_Euler"
t2 = "http://en.wikipedia.org/wiki/Kurt_Cobain"
t3 = "http://en.wikipedia.org/wiki/Nelson_Mandela"
t4 = "http://en.wikipedia.org/wiki/Leonardo_DaVinci"
t5 = "http://en.wikipedia.org/wiki/Archimedes"
f = urlopen(t4)
s = f.read()
f.close()

s = s.split("Died")

s[1] = s[1].split("td")
s[1][1] = s[1][1].split(">")
s[1][1][1] = s[1][1][1].split("<")


def findTheDeath(string): #sometimes works, mostly works
    f = urlopen(string)
    s = f.read()
    f.close()

    s = s.split("Died")

    s[1] = s[1].split("td")
    s[1][1] = s[1][1].split(">")
    s[1][1][1] = s[1][1][1].split("<")
    return s[1][1][1][0]
    
print findTheDeath(t4)

m = '''j = len(s[1][0])-1
ts1 = ""
while j > -1 and (s[1][0][j] != "<" and s[1][0][j] != ">") :
    ts1 = s[1][0][j] + ts1
    j-=1

j = 0
ts2 = ""
while j < len(s[1][1]) and (s[1][1][j] != "<" and s[1][1][j] != ">") :
    ts2 += s[1][1][j]
    j+=1


print s[1][0]
print "\n"
print s[1][1]
print ts1+ts2'''
