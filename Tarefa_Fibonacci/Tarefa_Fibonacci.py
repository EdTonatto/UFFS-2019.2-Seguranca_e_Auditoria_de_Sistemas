#Tarefa_Fibonacci
#URI 1153

identityMatrix = [[1, 0], [0, 1]]

def printMatrix(matrix):
	print("\nPrintando matriz:")
	for i in matrix:
		print(i)

def multiplyMatrix(matrixA, matrixB):
	matrixAns =[[0, 0], [0, 0]]
	matrixAns[0][0] = matrixA[0][0] * matrixB[0][0] + matrixA[0][1] * matrixB[1][0]
	matrixAns[0][1] = matrixA[0][0] * matrixB[0][1] + matrixA[0][1] * matrixB[1][1]
	matrixAns[1][0] = matrixA[1][0] * matrixB[0][0] + matrixA[1][1] * matrixB[1][0]
	matrixAns[1][1] = matrixA[1][0] * matrixB[0][1] + matrixA[1][1] * matrixB[1][1]
	return matrixAns

A = [[1, 2], [3, 4]]
B = [[-1, 3], [4, 2]]
printMatrix(A)
printMatrix(B)
multiplyMatrix(A, B)
X = multiplyMatrix(A, B)
printMatrix(X)
