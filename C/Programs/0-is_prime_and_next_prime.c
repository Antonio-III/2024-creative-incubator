#include <stdio.h>
#include <stdlib.h>

int isprime(int n);
int nextprime(int old_prime);

int main(int argc, char *argv[]){
    int n;
    printf("Enter a number: ");
    if (scanf("%d", &n)!=1){
        printf("No number entered!\n");
    }
    if (isprime(n)){
        printf("%d is a prime.\n", n);
    } else{
        printf("%d is not a prime.\n", n);
    }
    printf("%d is the next prime.\n",nextprime(n));
    return 0;
}

int isprime(int n){
    for (int divisor = 2; divisor * divisor <= n; divisor++){
        if (!(n % divisor)){
            return 0; 
            }
    }
    return 1;
}

int nextprime(int old_prime){
    int next_prime = old_prime + 1;
    while(!isprime(next_prime)){
        next_prime++;
    }
    return next_prime;
}