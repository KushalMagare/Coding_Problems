def printDiagonalSums(mat, n):
 
    principal = 0
    secondary = 0;
    for i in range(0, n):
        for j in range(0, n):
            if (i == j):
                principal += mat[i][j]
            if ((i + j) == (n - 1)):
                secondary += mat[i][j]
         
    print(principal)
    print(secondary)
 
a = [[ 2,3,0],
     [ 5,9,8 ],
     [7,6,3]]
printDiagonalSums(a, 3)