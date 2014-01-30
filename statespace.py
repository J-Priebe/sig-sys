
## INPUT:
#  
#
#
#
#
#
#
#
#




def getCoeffs():
    
    print ('Enter x(n-i)')
    print ('Enter y(n-k')
    print ('E.g., if your difference equation is y(n) = x(n-1) + 0.5x(n-3) + y(n-2)')
    print ('you would enter 1, 0, 0.5; then 0, 1')

    raw_x = raw_input().split(',')
    raw_y = raw_input().split(',')

    return ([int(x) for x in raw_x],
            [int(y) for y in raw_y])
 

# Coefficients are only important insomuch as they indicate
# whether the state has to be "remembered" or not
# This just checks if the coeff is non-zero, and if so, a
# assigns the term to a state
def printStates(coeffs):

    x_c = coeffs[0]
    y_c = coeffs[1]

    states = ""
    state_num = 1 

    for i in range(len(x_c)): # the x terms
        
        if x_c[i] != 0:
        
            s = "S"+str(state_num)+":  x(n - "+str(i+1)+")"
            states += s+"\n"
            state_num+= 1
            

    for i in range(len(y_c)): # the y terms

        if y_c[i] != 0:

            s = "S"+str(state_num)+":  y(n - "+str(i+1)+")"
            states += s+"\n"
            state_num+= 1


    print states




    




def main():
        
    printStates(getCoeffs())

    

if __name__ == "__main__":
        main()
