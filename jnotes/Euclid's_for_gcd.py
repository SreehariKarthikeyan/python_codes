''''
Euclid's algorithm for GCD:
a=64, b=48
1.Take larger number and write it in multiple of smaller
    64=48*1+16(rem)
2.Make left shift of all no.'s
    48=16*3+0
    16=0
3.When RHS is 0, LHS is the GCD.

Idea: GCD * LCM  =n1 *n2
'''


def ComputeGCD(a,b):
    '''Recursive func to change a nd b'''
    if b==0:
        return a
    else:
        return ComputeGCD(b,a%b)
 
def ComputeLCM(n1,n2):
    gcd=ComputeGCD(n1,n2)
    print(gcd)
    lcm=(n1*n2)/gcd
    return lcm



if __name__=='__main__':
    print(ComputeLCM(64,48))