import re
from math import *
import general_response as gr
import random

def all_arthimetic(expression):
    expression = expression.replace(' ', '')
    response = eval(expression)

    return response

# square root function


def sqrtFun(givenInput):
    sqrtResult=sqrt(int(givenInput))
    return sqrtResult
# Lateral surface area function


def LateralArea():
    pass
# total surface area function


def TotalsurfaceArea():
    pass
# volume function


def volume():
    pass
# power function


def power(givenInput, pwr):
    powResult= pow(int(givenInput),int(pwr))
    return powResult
# absoulte vale function


def absoluteValue(givenInput):
    all_arthimetics = ['+', '-', '*', '/']
    arthimetic=False
    number = givenInput.replace('|', '')
    sign_absolute = re.findall('\D', number)

    for i in sign_absolute:
        if i in all_arthimetics:
            arthimetic = True
        else:
            arthimetic = False
            break
    if arthimetic == True:
        c = all_arthimetic(number)
        absResult = abs(c)
    else:
        absResult = abs(int(number))
    return absResult
#


def quad(equation):

    # Remove whitespaces and split the equation into its components
    equation = equation.replace(" ", "")
    parts = equation.split("x^2")

    # Extract the coefficients a, b, and c
    a1 = parts[0]
    if a1 == '-':
        a = -1
    elif a1 == '':
        a=1
    else:
        a = float(parts[0])
    b1 = parts[1].split('x')[0]
    if b1 == '-':
        b = -1
    elif b1 == '+':
        b = 1
    else:
        b=float(parts[1].split('x')[0])
    c = float(parts[1].split("x")[1])

    # Calculate the discriminant
    discriminant = b ** 2 - 4 * a * c

    if discriminant > 0:
        # Two real and distinct roots
        root1 = (-b + sqrt(discriminant)) / (2 * a)
        root2 = (-b - sqrt(discriminant)) / (2 * a)
        root='{ '+str(root2)+", "+str(root1)+' }'
        return root
    elif discriminant == 0:
        # One real root (repeated)
        root = str(-b / (2 * a))
    else:
        # Complex roots
        root="No real root"
    return root



def mathChat(given,state):
    compare=list(gr.math_terms.keys())
    compare2=[]
    for k in compare:
        k = k.replace('-','')
        k = k.replace(' ', '')
        k = k.lower()
        compare2.append(k)
    if state == True:
        given=given.replace(' ','')
        given=given.replace('-','')
        given=given.replace('\n','')
        if given in compare2:
            index=compare2.index(given)
            term=list(gr.math_terms.keys())
            response=gr.math_terms[term[index]]
            no_term=False
        else:
            no_term=True
    else:
        given0 = []
        given0 = given.split(' ')
        no_term=True
                            
        
        for i in given0:
            i = i.replace(' ', '')
            i = i.replace('-', '')
            i = i.replace('\n','')
            if i in compare2:
                
                index=compare2.index(i)
                term=list(gr.math_terms.keys())
                response=gr.math_terms[term[index]]
                no_term=False
                break
            else:
                no_term=True
            
    if no_term == False:
        return response
    else:
        return gr.No_term_Response[random.randrange(len(gr.No_term_Response))]
