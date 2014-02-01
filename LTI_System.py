
## given a discrete system of the form
## y(n) = ax(n) + bx(n-1) .. cx(n-i) + py(n-1) + qy(n-2) .. ry(n-k)
## Gives the matrix ABCD/statespace representation,
## computes y(n), impulse response (h(n))


# get user to input the equation
# return tuple of x and y coefficients






def getCoeffs():

    print (
            'Enter the x and y coefficients of your system. For example,\n'
            'if your equation is   y(n) = x(n) + 0.5x(n-2) + 3y(n-1) you would enter\n'
            '0,0.5\n'
            '3\n'
            'Please enter only integers, decimals, and commas (no spaces)\n'
            'NOTE: remember that states starts at n-1; x(n) and y(n) are not states.\n'
           )
    
    raw_x = raw_input().split(',')
    raw_y = raw_input().split(',')

    return ([float(x) for x in raw_x],
            [float(y) for y in raw_y])
 

# input: tuple of x, y cofficients
# assigns states based on whether the coefficients are nonzero
def printStates(coeffs):

    x_c = coeffs[0]
    y_c = coeffs[1]


    #for i in range(


    states = []
    state_num = 1 

    for i in range(len(x_c)): # the x terms
        
        if x_c[i] != 0:

            states.append(state(state_num, "x", i+1))
        
            #s = "S"+str(state_num)+":  x(n - "+str(i+1)+")"
            #states += s+"\n"
            state_num+= 1
            

    for i in range(len(y_c)): # the y terms

        if y_c[i] != 0:

            states.append(state(state_num, "y", i+1))
            #s = "S"+str(state_num)+":  y(n - "+str(i+1)+")"
            #states += s+"\n"
            #state_num+= 1


    #print states
    for s in states:
        print s.to_string()


class state:
    def __init__(self, num, var, i):
        self.var = var
        self.num = num
        self.i = i

    def to_string(self):
        s = "S"+str(self.num)+":  "+self.var+"(n - "+str(self.i)+")"
        return s

    
        


class LTI_Syste




def main():
    print "Oh hai"
    

if __name__ == "__main__":
        main()
