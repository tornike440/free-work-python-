#a is integer
#b is also integer and both of them are least power of the whole f(x)
# c and d are coefficients of the f(x)
#matrix multiplication if just multiplication of a,c to b,d both of them being different f(x)es


def pollinomeMultiplication(c, d):
    a = c[0]
    b = d[0]
    realanswer = []
    answer = []

    for i in range(len(c)):
        first = []
        first.append(a + b + i)
        for j in d:
            first.append(c[i] * j)
        answer.append(first)

    for m in range(1, len(answer)):
        answer[m] = [0] * (m + 1) + answer[m][1:]

    max_length = max(len(row) for row in answer)
    for row in answer:
        while len(row) < max_length:
            row.append(0)

    for i in range(len(answer[0])):  # Sum columns
        total = 0
        for j in range(len(answer)):
            total += answer[j][i]
        realanswer.append(total)

    return realanswer



#now we two pollinoms in form of lists
#in both of the lists first element is least power of x
#and all the other ones are coefficients of the f(x)
#in the end we will get a list of the f(x)es in the form of [a,b,c,d,e,f,g,h]
def diffpowerpollinomeaddition(c,d):
    #first find out which power is the least
    #and add it to the answer

    #შევქმნათ ცარიელი პასუხი
    answer=[]
    if c[0]<d[0]:
        #add the first element of c to the answer
        answer.append(c[0])
        diff=d[0]-c[0]
        d[0]=0
        #add the rest of the elements of d to the answer
    else:
        #add the first element of d to the answer
        answer.append(d[0])
        diff=c[0]-d[0]
        c[0]=0
        #add the rest of the elements of c to the answer

    if len(c)<len(d):
        for i in range(0,diff):
            d.insert(1,0)
    else:
        for i in range(0,diff):
            c.insert(1,0)
        
    if len(c)>len(d):
        for i in range(0,len(c)-len(d)):
            d.append(0)
    else:
        for i in range(0,len(d)-len(c)):
            c.append(0)

    for i in range(0,len(c)):
        a=c[i]+d[i]
        answer.append(a)

    return answer

    


def matrixMultiplication(c,d):
    answer=[]
    firsmul=pollinomeMultiplication(c[0],d[0])
    secondmul=pollinomeMultiplication(c[1],d[3])
    thirdmul=pollinomeMultiplication(c[2],d[6])
    firstadd=diffpowerpollinomeaddition(firsmul,secondmul)
    secondadd=diffpowerpollinomeaddition(firstadd,thirdmul)
    answer.append(secondadd)

    
    firsmul=pollinomeMultiplication(c[0],d[1])
    secondmul=pollinomeMultiplication(c[1],d[4])
    thirdmul=pollinomeMultiplication(c[2],d[7])
    firstadd=diffpowerpollinomeaddition(firsmul,secondmul)
    secondadd=diffpowerpollinomeaddition(firstadd,thirdmul)
    answer.append(secondadd)

    
    firsmul=pollinomeMultiplication(c[0],d[2])
    secondmul=pollinomeMultiplication(c[1],d[5])
    thirdmul=pollinomeMultiplication(c[2],d[8])
    firstadd=diffpowerpollinomeaddition(firsmul,secondmul)
    secondadd=diffpowerpollinomeaddition(firstadd,thirdmul)
    answer.append(secondadd)





    firsmul=pollinomeMultiplication(c[3],d[0])
    secondmul=pollinomeMultiplication(c[4],d[3])
    thirdmul=pollinomeMultiplication(c[5],d[6])
    firstadd=diffpowerpollinomeaddition(firsmul,secondmul)
    secondadd=diffpowerpollinomeaddition(firstadd,thirdmul)
    answer.append(secondadd)

    firsmul=pollinomeMultiplication(c[4],d[1])
    secondmul=pollinomeMultiplication(c[5],d[4])
    thirdmul=pollinomeMultiplication(c[6],d[7])
    firstadd=diffpowerpollinomeaddition(firsmul,secondmul)
    secondadd=diffpowerpollinomeaddition(firstadd,thirdmul)
    answer.append(secondadd)


    firsmul=pollinomeMultiplication(c[3],d[2])
    secondmul=pollinomeMultiplication(c[4],d[5])
    thirdmul=pollinomeMultiplication(c[5],d[8])
    firstadd=diffpowerpollinomeaddition(firsmul,secondmul)
    secondadd=diffpowerpollinomeaddition(firstadd,thirdmul)
    answer.append(secondadd)



    firsmul=pollinomeMultiplication(c[6],d[0])
    secondmul=pollinomeMultiplication(c[7],d[3])
    thirdmul=pollinomeMultiplication(c[8],d[6])
    firstadd=diffpowerpollinomeaddition(firsmul,secondmul)
    secondadd=diffpowerpollinomeaddition(firstadd,thirdmul)
    answer.append(secondadd)


    firsmul=pollinomeMultiplication(c[6],d[1])
    secondmul=pollinomeMultiplication(c[7],d[4])
    thirdmul=pollinomeMultiplication(c[8],d[7])
    firstadd=diffpowerpollinomeaddition(firsmul,secondmul)
    secondadd=diffpowerpollinomeaddition(firstadd,thirdmul)
    answer.append(secondadd)

    firsmul=pollinomeMultiplication(c[6],d[2])
    secondmul=pollinomeMultiplication(c[7],d[5])
    thirdmul=pollinomeMultiplication(c[8],d[8])
    firstadd=diffpowerpollinomeaddition(firsmul,secondmul)
    secondadd=diffpowerpollinomeaddition(firstadd,thirdmul)
    answer.append(secondadd)

    return answer



import re
from collections import defaultdict

def removeZeroes(string):
    terms = string.split(" + ")
    terms = [term for term in terms if not term.startswith("0*")]
    return " + ".join(terms) if terms else "0"

def distribute_symbolic(symbol_str, multiplier):
    """
    Takes a symbolic expression like '3a + b' and an integer multiplier,
    and returns the expanded version like '6a + 2b'
    """
    terms = symbol_str.replace("-", "+-").split("+")
    result_terms = []

    for term in terms:
        term = term.strip()
        if not term:
            continue
        match = re.match(r"(-?\d*)([a-zA-Z].*)", term)
        if match:
            coeff_str, var_part = match.groups()
            coeff = int(coeff_str) if coeff_str not in ("", "+", "-") else int(coeff_str + "1") if coeff_str else 1
            new_coeff = coeff * multiplier
            result_terms.append(f"{new_coeff}{var_part}")
        else:
            # It's likely just a variable like 'b'
            result_terms.append(f"{multiplier}*{term}")
    return " + ".join(result_terms)

def symbolicPolynomialMultiplication(c, d):
    if not isinstance(c[0], int) or not isinstance(d[0], int):
        raise ValueError("First elements of both lists must be integers (starting powers)")

    a = c[0]
    b = d[0]
    poly_c = c[1:]
    poly_d = d[1:]

    for val in poly_d:
        if not isinstance(val, int):
            raise ValueError("All elements in d (after the first) must be integers")

    terms = defaultdict(lambda: defaultdict(int))  # {power: {symbol: coefficient}}

    for i, coeff_c in enumerate(poly_c):
        for j, coeff_d in enumerate(poly_d):
            power = a + b + i + j
            symbol_expr = coeff_c

            if isinstance(symbol_expr, str):
                # Distribute the integer coeff_d into the symbolic expression
                distributed = distribute_symbolic(symbol_expr, coeff_d)
                for term in distributed.split(" + "):
                    match = re.match(r"(-?\d+)\*?(.+)", term.strip())
                    if match:
                        count, symbol = match.groups()
                        terms[power][symbol] += int(count)
            else:
                # It's a raw integer or unsupported format
                symbol = str(symbol_expr)
                terms[power][symbol] += coeff_d

    result = []
    min_power = min(terms)
    max_power = max(terms)

    for p in range(min_power, max_power + 1):
        if p in terms:
            parts = []
            for symbol, count in terms[p].items():
                if count == 1:
                    parts.append(f"{symbol}")
                else:
                    parts.append(f"{count}*{symbol}")
            result.append(" + ".join(parts))
        else:
            result.append("0")

    result.insert(0, min_power)

    for i in range(1, len(result)):
        result[i] = removeZeroes(result[i])

    return result

def addSymbolicPolynomials(c, d):
    """
    Adds two symbolic polynomials with possibly different starting powers.
    Each polynomial is a list where the first element is the least power,
    and the rest are string expressions (like "2a + b").
    """
    # Determine starting powers
    power_c = c[0]
    power_d = d[0]
    
    # Determine new starting power
    min_power = min(power_c, power_d)

    # Create aligned lists with padding
    pad_c = ["0"] * (power_d - power_c) if power_c < power_d else []
    pad_d = ["0"] * (power_c - power_d) if power_d < power_c else []

    coeffs_c = pad_c + c[1:]
    coeffs_d = pad_d + d[1:]

    # Pad shorter list to match lengths
    max_len = max(len(coeffs_c), len(coeffs_d))
    coeffs_c += ["0"] * (max_len - len(coeffs_c))
    coeffs_d += ["0"] * (max_len - len(coeffs_d))

    # Combine symbolic terms
    result = [min_power]
    for term_c, term_d in zip(coeffs_c, coeffs_d):
        if term_c == "0":
            result.append(term_d)
        elif term_d == "0":
            result.append(term_c)
        else:
            result.append(f"{term_c} + {term_d}")

    # Optional: clean up using removeZeroes (if needed)
    for i in range(1, len(result)):
        result[i] = removeZeroes(result[i])

    return result

a=[[0, 0], [-1, -1], [0, 1], [-3, 1], [-1,-2], [0,1], [0,0], [0,0], [0,0]]
b=[[0,1], [0,0], [0,0], [0,0], [0,1], [0,0], [0,0], [0,1], [1,-1]]
c=[[1,-1], [0,1],[0,0], [0,-1], [0,0], [0,1], [0,-1,1], [0,0], [0,1]]
d=[[0,0], [0,-1], [0,1], [0,0], [0,-1], [0,0], [1,-1], [0,-1,1], [0,0]]
v=[[0,"2a+3b","a+2c"], [0,"2a+3b","a+2c"], [2,"-2a-3b","d"]]


answer=[]
while True:
    ask=input("enter which matrix you want to multiply:")
    match ask:
        case "a":
            for i in range(0,3):
                firstmul=symbolicPolynomialMultiplication(v[0],a[i])
                secondmul=symbolicPolynomialMultiplication(v[1],a[i+3])
                thirdmul=symbolicPolynomialMultiplication(v[2],a[i+6])
                answer.append(addSymbolicPolynomials(addSymbolicPolynomials(firstmul,secondmul),thirdmul))
                v=answer
            answer=[]
            

        case "b":
            for i in range(0,3):
                firstmul=symbolicPolynomialMultiplication(v[0],b[i])
                secondmul=symbolicPolynomialMultiplication(v[1],b[i+3])
                thirdmul=symbolicPolynomialMultiplication(v[2],b[i+6])
                answer.append(addSymbolicPolynomials(addSymbolicPolynomials(firstmul,secondmul),thirdmul))
                v=answer
            answer=[]
            
        case "c":
            for i in range(0,3):
                firstmul=symbolicPolynomialMultiplication(v[0],c[i])
                secondmul=symbolicPolynomialMultiplication(v[1],c[i+3])
                thirdmul=symbolicPolynomialMultiplication(v[2],c[i+6])
                answer.append(addSymbolicPolynomials(addSymbolicPolynomials(firstmul,secondmul),thirdmul))
                v=answer
            answer=[]
            
        case "d":
            for i in range(0,3):
                firstmul=symbolicPolynomialMultiplication(v[0],d[i])
                secondmul=symbolicPolynomialMultiplication(v[1],d[i+3])
                thirdmul=symbolicPolynomialMultiplication(v[2],d[i+6])
                answer.append(addSymbolicPolynomials(addSymbolicPolynomials(firstmul,secondmul),thirdmul))
                v=answer
            answer=[]
            
        case "x":
            print(f"final answer is {v}")
            print("exit")
            break
    print(v[0])
    print(v[1])
    print(v[2])


        
        
            













    







    



# def getMatrixReady():
#     a=[]
#     for i in range(0,10):
#         polinome=[]
#         m=int(input("least power of x:"))
#         polinome.append(m)
#         n=int(input("number of coefficients:"))
#         for j in range(0,n):
#             coeff=int(input("coeff:"))
#             polinome.append(coeff)
#         a.append(polinome)

#     for i in range(0,len(a)):
#         print("polinome", a[i])

#     return a




    
# firstMatrix=getMatrixReady()
# secondMatrix=getMatrixReady()
# thirdMatrix=getMatrixReady()
# fourthMatrix=getMatrixReady()
