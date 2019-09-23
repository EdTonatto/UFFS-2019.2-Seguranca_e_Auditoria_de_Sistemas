//Tarefa_Fibonacci
//URI 1153
#include <stdio.h>

void printMatrix(int matrix[2][2]){
	int i = 0, j = 0;
	printf("Printando Matriz:\n");
	printf(" | 0 | 1\n");
	printf("---------\n");
	for(i = 0; i < 2; i++){
		printf("%d| ", i);
		for(j = 0; j < 2; j++){
			if(j%2 == 0)
				printf("%d | ", matrix[i][j]);
			else
				printf("%d", matrix[i][j]);
		}
		if(i%2 == 0) printf("\n---------\n");
	}
}

int main(){
	int A[2][2] = {{1, 2}, {3, 4}};
	int B[2][2] = {{-1, 3}, {4, 2}};
	
	printMatrix(A);
	
	return 0;
}