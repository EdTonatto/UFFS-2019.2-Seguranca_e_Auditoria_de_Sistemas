#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef long long ll;

int x, y, d;

int calculate_phi(int n){
  int result = n;

  for(int i = 2; i * i <= n; i++){
    if(n % i == 0){
      while(n % i == 0)
        n /= i;
      result -= result / i;
    }
  }
  if(n > 1)
    result -= result / n;

  return result;
}

void euclid_ext(int a, int b){
  if(!b){
    x = 1;
    y = 0;
    d = a;
    return;
  }
  euclid_ext(b, a % b);

  int x1 = y, y1 = x - (a / b) * y;
  x = x1, y = y1;
}

int inv_mod(int a, int m){
  euclid_ext(a, m);
  return (x % m + m) % m;
}

ll fast_exp(ll p, ll q, ll m){
  ll r = 1;
  while(q){
    if(q & 1)
      r = (r * p) % m;
    p = (p * p) % m;
    q >>= 1;
  }
  return r;
}

int main(){
  int n, e, c, phi;

  scanf("%d %d %d", &n, &e, &c);
  phi = calculate_phi(n);

  int d = inv_mod(e, phi);
  printf("%lld\n", fast_exp(c, d, n));

  return 0;
}
