#include <stdio.h>
#include <math.h>


//factorial function
int Myfactorial(int n) {
    if (n < 0) {
        printf("Error\n");
        return -1; 
    }
    if (n == 0) {
        return 1; 
    }
    else {
        return n * Myfactorial(n - 1);
    }
}

void main() {
    int test = 5;
    int factorial = Myfactorial(test);
    printf("Factorial of %d is %d\n", test, factorial);

    double expoTest = 3.0;
    exp(expoTest);
    printf("Exponential of %.4f is %.4f\n", expoTest, exp(expoTest));

    double logTest = 10.0;
    log(logTest);
    printf("Ln of %.4f is %.4f\n", logTest, log(logTest));

    

}