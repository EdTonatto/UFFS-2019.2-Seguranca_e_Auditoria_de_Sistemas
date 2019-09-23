#Tarefa_Fibonacci
#URI 1153

identityMatrix = [[1, 0], [0, 1]]
baseMatrix = [[0, 1], [1, 1]]

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

def expMatrix(matrixA, exp):
	matrixAns = [[0, 0], [0, 0]]
	if exp == 0:
		return identityMatrix
		
	if exp%2 == 1:
		return multiplyMatrix(matrixA, expMatrix(matrixA, (exp - 1)))
		
	matrixAns = expMatrix(matrixA, exp/2)
	return multiplyMatrix(matrixAns, matrixAns)
	
def fibonacci(num):
	matrixFib = expMatrix(baseMatrix, num)
	return matrixFib[0][1]

print(fibonacci(78))

