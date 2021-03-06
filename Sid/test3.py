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
        return [a[0],True]
    else:
        return [a[0] + "-(" + a[1] + ")",False]

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
    y =(detectVariables(a[0])).items() #we now have dependent variables and independent variables
    t = 0
    b = []
    q = 0
    for m in y:
        if m[1] == 't':
            t = m[0]
        if m[1] == 'a':
            b.append(m[0])
    if b == []:
        b = ["x"]

   
            
    symboltable = ""
    for lambs in b:
        symboltable += (lambs+"=Symbol(\""+lambs+"\")\n")
        
    if a[1]:
            
            a = a[0]
                        
            if t != 0: #We are dealing with a differential equation
                a = ctp(a,b[0],t) #converting everything to a diff that is function in variable b[0]

                symboltable +=t+"=Symbol(\""+t+"\")\n"
                exec("from sympy import *\n"+symboltable+
                     "a = str(simplify("+a+"))") #cleaned up expression
                return "Simplified Functional Expression Expression to: " + a
              
            else:
                exec("from sympy import *\n"+
                     symboltable+
                     "a = str(simplify("+a+"))") #cleaned up non variable expression
                return "Simplified Algebraic Expression to: " + a
             
            
    else:
            a = a[0]
          
            
            if t != 0: #We are dealing with a differential equation
                
                a = ctp(a,b[0],t) #converting everything to a diff that is function in variable b[0]

                symboltable +=t+"=Symbol(\""+t+"\")\n"
                exec("from sympy import *\n"+symboltable+
                     "a = str(simplify("+a+"))") #cleaned up expression
                print "Simplified Functional Expression Expression to: " + a
                try:
                    exec("from sympy import *\n"+
                         symboltable+
                         "q=dsolve("+a+")") #evaluate code
                    return q
                except:
                    return "I must consult with the elders on this functional equation"
            else:

                
                
                exec("from sympy import *\n"+
                     symboltable+
                     "a = str(simplify("+a+"))") #cleaned up non variable expression
                print "Standardized Algebraic Expression to: " + a + "=0"
                try:
                    exec("from sympy import *\n"+
                         symboltable+
                         "q = solve("+a+","+b[0]+")\n")
                    return q
                
                except:
                    return "This one is a challenge indeed, call me tomorrow babycakes ;)"
        


# x = "y''-2y'+5y=0"
# 
# while True:
# 
#     x = raw_input("Enter Expression for Processing: ")
#     if x == "e":
#         break
#     else:
#         print solver(x)
        




