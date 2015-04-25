from sympy import *
#Notes: Sid is cool
#btw email biglars@cs.rutgers.edu for internship
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


def ctp(string, argvar, typevar):
        s = string
        sn = s
        sn = sn.replace("'",".diff("+argvar+")")
        while sn != s:
            s = sn
            sn = sn.replace("'",".diff("+argvar+")")
        sn = sn.replace(typevar,typevar+"("+argvar+")")
        m = exec(""+argvar+"=Symbol('"+argvar+"')\n"+typevar+"=Function('"+typevar+"')\nprint dsolve("+sn+")")
        return m

    
x = "y'-y"

pprint(ctp("2*x**2*y''+y'",'x','y'))

