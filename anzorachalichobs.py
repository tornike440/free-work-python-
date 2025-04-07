#a is integer
#b is also integer and both of them are least power of the whole f(x)
# c and d are coefficients of the f(x)
#matrix multiplication if just multiplication of a,c to b,d both of them being different f(x)es


def mult(c, d):
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
def add(c,d):
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

    




firstmatrix=[[0, 0], [-1, -1], [0, 1], [-3, 1], [-1,-2], [0,1], [0,0], [0,0], [0,0]]
secondmatrix=[[0,1], [0,0], [0,0], [0,0], [0,1], [0,0], [0,0], [0,1], [1,-1]]
thirdmatrix=[[1,-1], [0,1],[0,0], [0,-1], [0,0], [0,1], [0,-1,1], [0,0], [0,1]]
fourthmatrix=[[0,0], [0,-1], [0,1], [0,0], [0,-1], [0,0], [1,-1], [0,-1,1], [0,0]]


def matrixMultiplication(c,d):
    answer=[]
    for i in range(0,3):
        for j in range(0,3):    
            
            firsmul=mult(c[0+3*i],d[0+j])
            secondmul=mult(c[1+3*i],d[3+j])
            thirdmul=mult(c[2+3*i],d[6+j])
            firstadd=add(firsmul,secondmul)
            secondadd=add(firstadd,thirdmul)
            answer.append(secondadd)

           
    return answer

print(matrixMultiplication(firstmatrix,secondmatrix))




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
