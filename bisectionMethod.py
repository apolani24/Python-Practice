import matplotlib.pyplot as plt
import scipy

degree = input("What degree is your polynomial? ")

polyList = []

for i in range(int(degree) + 1):
    n = input("Enter the term: ")
    polyList.append(int(n))
print(polyList)

poly = scipy.poly1d(polyList)




def bisect(f,a,b,n):
    count = 0
    while(count != n):
        c = (a+b) / 2
        d = f(c) * f(a)
        if(d < 0):
            b = c
        elif(d > 0):
            a = c
        else:
            print("C is exactly correct.", c)
            return(c)
        count = count + 1
    print(c)


bisect(poly,0,4,1000)


# Things to do, not extensive
# Print out the polynomial in the proper form
# Print out explicitly what is happening
# Fix the enter the term bit
# Comment the code, help function
# Add options for tuning endpoints and error term
