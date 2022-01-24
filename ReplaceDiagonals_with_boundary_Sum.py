'''Replace Diagonals'''

def ReplaceDiagonal (mat):
    '''Replaces the diagonal elements with the sum of the boundary elements of diagonal. Each diagonal element should consider the previously calculated diagonal value, not the orignal diagonal value'''
    n=len(mat)-1
    #first element and last element of diagonal always have only 3 boundary values, whereas middle elements have exactly 8 boundary values.
    mat[0][0]=mat[0][1]+mat[1][1]+ mat[1][0]
    if n >1:
        for i in range (1,n):
            mat[i][i] = mat[i-1][i-1]+mat[i-1][i]+mat[i-1][i+1] + mat[i][i-1]+mat[i][i+1] + mat[i+1][i-1]+mat[i+1][i]+mat[i+1][i+1]

    mat[n][n]=mat[n][n-1]+mat[n-1][n]+mat[n-1][n-1]
    return mat

if __name__=='__main__':

    mat=list([[ 1, 2, 3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
    mat=ReplaceDiagonal (mat)
    for i in mat:
        print(i)