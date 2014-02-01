
## given a discrete system of the form
## y(n) = ax(n) + bx(n-1) .. cx(n-i) + py(n-1) + qy(n-2) .. ry(n-k)
## Gives the matrix ABCD/statespace representation,
## computes y(n), impulse response (h(n))


# get user to input the equation
# return tuple of x and y coefficients




class LTI_System:

    # takes float coeff on x(n) term, tuple of x, y coeffs on states (e.g, x(n-1), y(n-2))
    def __init__(self, input_coeff, state_coeffs):

        self.input_coefficient = input_coeff
        states = []

        i = 1
        for c in state_coeffs[0]: # x coefficients
            states.append(self.State('x', c, i)) 
            i += 1   

        k = 1
        for c in state_coeffs[1]: # y coefficients
            states.append(self.State('y', c, k))
            k += 1

        self.states = states
     


    def print_states(self):
        num = 1
        for s in self.states:
            print "S"+str(num)+": "+s.to_string()
            next_state = self.State(s.var, s.coeff, s.i - 1)
            print "Next state:  "+ next_state.to_string()
            num += 1

    def print_equation(self):  #####
        eq = "y(n) = "
        for s in self.states:
            eq += "+ "+s.to_string()
        print eq

    def get_ABCD(self): # return (A, B, C, D)
        size = len(self.states)
        A = [None]*size
        B = [None]*size
        for i in range(size):
            A[i] = [0.0] * size
            B[i] = [0.0]
        C = [0]*size
        D = [self.input_coefficient]

        # C
        for i in range  (size):
            C[i] = self.states[i].coeff
        
        # A and B
        for i in range (size):
            state = self.states[i]
            next_state = self.State(state.var, state.coeff, state.i - 1)                  
            # three possiblities
            # 1. next state = x(n)
            # 2. next state = y(n) = all states
            # 3. next state = another state
            
            # 1.
            if (next_state.i == 0 and next_state.var == 'x') :
                B[i][0] = 1
            # 2.
            elif (next_state.i == 0 and next_state.var == 'y') :
                for k in range (size):
                    A[i][k] = self.states[k].coeff
                B[i][0] = self.input_coefficient
            # 3.
            else :
                for k in range (size):
                    if next_state.equals(self.states[k]):
                        A[i][k] = 1
        return (A, B, C, D)


    class State:
        def __init__(self, var, coeff, i):
            self.coeff =  coeff
            self.var = var
            self.i = i

        def to_string(self):
            s = self.var+"(n - "+str(self.i)+")"
            return s

        def equals(self, state):
            if (self.i == state.i and self.var == state.var):
                return True
            else:
                return False

# interactively make LTI System.
# When called from other classes, use manual contructor
def main():
    print (
    'Enter the x and y coefficients of your system. For example,\n'
    'if your equation is   y(n) = x(n) + 0.5x(n-2) + 3y(n-1) you would enter\n'
    '0,0.5\n'
    '3\n'
    'Please enter only integers, decimals, and commas (no spaces)\n'
    'NOTE: remember that states start at n-1; x(n) and y(n) are not states.\n'
    )
    raw_x = raw_input().split(',')
    raw_y = raw_input().split(',')
    state_coeffs = ([float (x) for x in raw_x],
                    [float (y) for y in raw_y],
                    )
    print ('Enter the coefficient on x(n)')
    x_coeff = float(raw_input())
    system = LTI_System(x_coeff, state_coeffs)
    # system.print_equation()
    print 'states:\n'
    system.print_states()
    print '\n'
    abcd = system.get_ABCD()
    print 'A:    '+str(abcd[0])
    print 'B:    '+str(abcd[1])
    print 'C:    '+str(abcd[2])
    print 'D:    '+str(abcd[3])
    

if __name__ == "__main__":
        main()
