from sympy import *
import sympy as sp

directory = "E:\OneDrive - IIT Delhi\CODE\Deadly_Python\SOLVER\History.txt"
f1=open(directory,"r+")

x,y,z,a,b,c=sp.symbols('x y z a b c')
f=Function('f')(x,y,z)
g=Function('g')(x,y,z)
h=Function('h')(x,y,z)
p=Function('p')(x,y,z)
q=Function('q')(x,y,z)
funcsions = [f,g,h,p,q]

def soln_parser(s):                         # For printing data in pretty format
    s=s.replace('\/`','√').replace('**','^').replace('*',' × ').replace('exp','𝓮^')
    s=s.replace('e^', '𝓮^').replace('x','𝓍').replace('y','𝓎').replace('z','𝔃').replace('f','𝓯').replace('g','𝓰')
    
    return s

def anti_parser(s):                         # For storing in string format
    s=s.replace(',',' =').replace('sqrt','\/`').replace('**','^')
    s=s.replace('exp', 'e^') 

    return s

def function_parser(s):						# Converting input to differentiable and integrable form
    s=s.replace('sqrt','sp.sqrt').replace('e^','exp')
    s=s.replace('sin','sp.sin').replace('asp.sin','sp.asin')
    s=s.replace('csc','sp.csc').replace('asp.csc','sp.acsc')
    s=s.replace('cos','sp.cos').replace('asp.cos','sp.cos')
    s=s.replace('sec','sp.sec').replace('asp.sec','sp.sec')
    s=s.replace('tan','sp.tan').replace('asp.tan','sp.atan')
    s=s.replace('cot','sp.cot').replace('asp.cot','sp.acot')
    s=s.replace('log', 'sp.log').replace('abs', 'sp.Abs').replace('^','**')

    return eval(s)

def set_functions(fnk):
    
    options = "No of functions : 1-5\nNOTE:- MAX 5 custom functions can be selected : <f,g,h,p,q>\n\nPress ENTER to SKIP choosing functions\n"
    print("\nPreset Function Editor")
    print(f"{options}")
    
    
    global funcsions
    
    op_f = input("Enter Choice : ")

    if fnk ==[]:
        fns = [f,g,h,p,q]

        if op_f.isdigit() and int(op_f) <= 5 :
            for i in range(int(op_f)):
                fn = (input(f"Enter function {funcsions[i]} : "))
                if fn == '':
                    pass
                else:
                    try:
                        fns[i] = function_parser(fn)
                    except:
                        pass
            return fns

        else:
            print("# No usable functions taken #")
            return []
    
    else:
        fns = fnk
        
        if op_f.isdigit() and int(op_f) <= 5 :
            print("Press ENTER to skip")

            for i in range(int(op_f)):
                fn = (input(f"Enter function {funcsions[i]} : "))
                if fn == '' :
                    print(f"{funcsions[i]} = {fnk[i]}")
                else:
                    try:
                        fns[i] = function_parser(fn)
                    except:
                        print("!! Invalid Function !!")
                        print('Skipped')
            return fns
        
        else:
            return fns

def get_var(f,n):
    _var = None
    ftype = None
    if 'x' in f:
        if ('y' in f) or ('z' in f) :
            ftype = 'multivariable'
        else:
            ftype = 'singlevariable'
            _var = 'x'

    elif 'y'in f:
        if 'z' in f:
            ftype = 'multivariable'
        else:
            ftype = 'singlevariable'
            _var = 'y'
    else:
        ftype = 'singlevariable'
        _var = 'z'

    var_list = []
    if ftype == 'singlevariable':
        for i in range(n):
            var_list.append(_var)

    elif ftype == 'multivariable':
        var_list = list(input(f"Specify order of differentiation variables <with spaces> to differentiate {f}: ").split())
        if len(var_list) < n :
            _var = input("Specify variable for the rest of the differentiation : ")
            a = len(var_list)
            var_list.extend([_var]*(n-a))
    
    return var_list

def Differentiator():
        print()
        print("=== Function Differentiator ===")
        
        funksans = set_functions([])
        if funksans != []:
            f,g,h,p,q = funksans
        
        while True:
            try :
                expression = input("\nEnter expression (q to quit): ")

                if expression == 'q':
                    break

                if expression == '':
                    print("!! Expression can't be empty !!")
                    print("!! Try Again !!")

                elif expression == 'showfns':

                    if funksans != []:
                        fn_counter=0
                        print("Preset functions : ")
                        for i in range(5):
                            if str(type(funksans[i])) not in 'fghpq':
                                print(f"{fn_counter+1}. {funcsions[i]} = {funksans[i]}")
                                fn_counter+=1
                    else:
                        print("!! No preset functions available !!")
                
                elif expression == 'setfn':
                    funksans = set_functions(list(funksans))
                    if funksans != []:
                        f,g,h,p,q = funksans

                else:
                    f_eqn = str(eval(expression))
                    f_print = soln_parser(f_eqn)
                    f_diff = function_parser(f_eqn)
                    
                    n=int(input("Enter the number of times to differentiate : "))
                    if n<1 :
                        print("Error : Order can only be a positive Real number")
                        
                    print()
                    
                    try :
                        var_diff = get_var(f_eqn,n)
                        print(f"Function is : {f_print}")
                        for i in range(n):
                                dvar = var_diff[i]
                                f_diff = f_diff.diff(dvar)
                                f_pretty = soln_parser(str(f_diff))
                                print("Differentiated with respect to {} ; {} =".format(var_diff[i],'F'+'\''*(i+1)),f_pretty)

                    except Exception as e:
                        print(f"Error : {e}")
            
            except Exception as e:
                print(f"Error : {e}")

Differentiator()