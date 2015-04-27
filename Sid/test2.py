from sympy import *
#Notes: Sid is cool
#@Matt Goldman you want all these methods, your target method is SOLVER which accepts a string and solves it!
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
    return sn
    #exec(argvar+"=Symbol('"+argvar+"')\n"+typevar+"=Function('"+typevar+"')\nq=dsolve("+sn+")")
    

def mathparseRoland(a): #From Rolan=ROland=Nolan=Noland=No Land
    a = ''.join(a.split()) #remove white space
    a = a.replace("^", "**")
    a = list(a)
    
    i = 0
    while i < len(a):
        if a[i].isalpha():
            if i != 0:
                if a[i-1] != "+" and a[i-1] != "/" and a[i-1] != "*" and a[i-1] != "-" and a[i-1] != "=":
                    a.insert(i,'*')
                    i+=1
            
            while i < len(a) and a[i].isalpha():
                i+=1
            i-=1
        i+=1
            
    a = ''.join(a)
    a = a.split("=") #split by equality sign if present
    if len(a) == 1:
        return a[0]
    else:
        return a[0] + "-(" + a[1] + ")"

def detectVariables(a):
    argvar = {}
    x = ""
    i = 0
    j = 0
    while i < len(a):
        while i < len(a) and a[i].isalpha(): #begin identifying substring
            x += a[i] #add the letter detected
            i+=1
        if i < len(a) and len(x) != 0 and a[i] == "'":
            try:
                if argvar[x] == 'a':
                    argvar[x] = 't'
            except:
                argvar[x] = 't'
            x = ""
          

        if len(x) != 0:
            try:
                if argvar[x] == 't':
                    argvar[x] = 't'
            except:
                argvar[x] = 'a'
            x = ""
        
        i+=1
    return argvar

def solver(a):
    a = mathparseRoland(a) #processes items
   
    y =(detectVariables(a)).items() #we now have dependent variables and independent variables
    t = 0
    b = 0
    q = 0
    for m in y:
        if m[1] == 't':
            t = m[0]
        if m[1] == 'a':
            b = m[0]
        if t != 0 and b != 0:
            break
    if b == 0:
        b = "x"

    
    
    if t != 0: #We are dealing with a differential equation
        a = ctp(a,b,t) #converting everything to a diff
        exec("from sympy import *\n"+
             b+"=Symbol(\""+b + "\")\n"+
             t+"=Symbol(\""+t+"\")\n"+
             "a = str(simplify("+a+"))") #cleaned up expression
        print "Standardized Functional Expression to: " + a + "=0"
        try:
            exec("from sympy import *\n"+
                 b+"=Symbol(\""+b + "\")\n"+
                 t+"=Function(\""+t+"\")\n"+
                 "q=dsolve("+a+")") #evaluate code
            print q
        except:
            print "I must consult with the elders on this functional equation"
    else:
        exec("from sympy import *\n"+
             b+"=Symbol(\""+b + "\")\n"+
             "a = str(simplify("+a+"))") #cleaned up non variable expression
        print "Standardized Algebraic Expression to: " + a + "=0"
        try:
            exec("from sympy import *\n"+
                 "q = solve("+a+","+b+")\n")
            print q
        except:
            print "This one is a challenge indeed"
        

x = "y''-2y'+5y=0"

while True:

    x = raw_input("Enter Expression for Processing: ")
    if x == "e":
        break
    else:
        solver(x)
        




