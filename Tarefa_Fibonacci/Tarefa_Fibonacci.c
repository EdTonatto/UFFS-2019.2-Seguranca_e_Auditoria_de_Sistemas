//Tarefa_Fibonacci
//URI 1153
#include <stdio.h>

void printMatrix(int matrix[2][2]){
	int i = 0, j = 0;
	printf("\nPrintando Matriz:\n");
	printf("  | %4d | %4d\n", i, j);
	printf("---------------\n");
	for(i = 0; i < 2; i++){
		printf("%2d| ", i);
		for(j = 0; j < 2; j++){
			if(j%2 == 0)
				printf("%4d | ", matrix[i][j]);
			else
				printf("%4d", matrix[i][j]);
		}
		if(i%2 == 0) printf("\n---------------\n");
	}
}

void multiplyMatrix(int matrixA[2][2], int matrixB[2][2], int matrixAns[2][2]){
	matrixAns[0][0] = matrixA[0][0] * matrixB[0][0] + matrixA[0][1] * matrixB[1][0];
	matrixAns[0][1] = matrixA[0][0] * matrixB[0][1] + matrixA[0][1] * matrixB[1][1];
	matrixAns[1][0] = matrixA[1][0] * matrixB[0][0] + matrixA[1][1] * matrixB[1][0];
	matrixAns[1][1] = matrixA[1][0] * matrixB[0][1] + matrixA[1][1] * matrixB[1][1];
}

int main(){
	int A[2][2] = {{5, 5}, {6, 6}};
	int B[2][2] = {{9, 9}, {9, 9}};
	int X[2][2];
	
	printMatrix(A);
	printMatrix(B);
	multiplyMatrix(A, B, X);
	printMatrix(X);
	
	return 0;
}