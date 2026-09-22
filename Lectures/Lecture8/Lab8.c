#include <stdio.h>
#include <math.h>
//factorial function
double Myfactorial(int n) {
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

double expo(double x, double initial, int kmax, double tol){
    double s = initial;
    if(x == 0){
        return 1.0;
    }
    for (int k = 1; k < kmax; k++) {
        double sold = s;
        s = s + (pow(x, k) / Myfactorial(k));
        if (s != 0) {
            if (fabs(s - sold) / abs(s) < tol) {
                break;
            }
        }
    }
    return s;
}

void main() {
    double pointSet[] = {0.0, 0.02, 0.04, 0.06, 0.1, 0.15, 0.18, 0.2, .22, 0.25, 0.3, 0.33, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.73, 0.75, 0.8, 0.83, 0.85, 0.9, 0.95, 0.97, 1.0};
    int numPoints = 29;

    for (int i = 0; i < numPoints; i++) {
        double x = pointSet[i];
        double result = expo(x, 1.0, 100, 1e-14);
        printf("%.14f\n", result);

    }
}