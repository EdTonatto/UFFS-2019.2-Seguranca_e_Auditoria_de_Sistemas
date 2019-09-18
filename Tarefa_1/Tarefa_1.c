//Tarefa_1
#include <stdio.h>

int tunel[112];

int gcd(int x, int y){
	if(y == 0)
		return x;
	return gcd(y, x%y);
}

int main(){
	int n, i;
	scanf("%d", &n);
	
	for(i = 1; i <= n; i++)
		scanf("%d", &tunel[i]); 
	
	int resultado = -1;
	
	for(i = 1; i <= n; i++){
		if(tunel[i]){
			int count = 0;
			int atual = i;
			while(tunel[atual]){
				count++;
				int proximo = tunel[atual];
				tunel[atual] = 0;
				atual = proximo;
			}
			if(resultado < 0)
				resultado = count;
			resultado = (resultado / gcd(resultado, count) * count);
		}
	}
	printf("%d\n", resultado);
	
	return 0;
}