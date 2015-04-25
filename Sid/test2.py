from sympy import *

#biglars@cs.rutgers.edu
def piplist(list1,point,list2):
        i = 0
        p = point
        while i < len(list2):
            if p+i <= len(list1):
                list1.insert(p+i,list2[i])
            else:
                list1.append(list2[i])
            i+=1
        return list1
m = '''def ctp(string):
    t = list(string)
    
    i = 0
    while i < len(t):
        if t[i] == "'":
            t.pop(i)
            j = i-1
            while t[j].isalpha() and j > -1:
                j-=1
            try:
                print t[j],j
            except:
                print j
            j+=1
          
            t.insert(j,"(")
            t = piplist(t,i+1,list(").diff(x)"))
           
        i+=1
    return ''.join(t)'''


def pfts(string): #properly format that shit

    def ctp(string):
        s = string
        sn = s
        sn = sn.replace("'",".diff(x)")
        while sn != s:
            s = sn
            sn = sn.replace("'",".diff(x)")
        return sn
 
    return ctp(string)
x = "y(x)'-y(x)"

print pfts(x)
exec("x=Symbol('x')\ny=Function('y')\nprint dsolve("+pfts(x)+")")

