#include <stdio.h>
#include <stddef.h>
#include <stdlib.h>
#include <string.h>

int main(){
    int A = 2107483647;
    int B = 100000;
    while (B != 0) {
        int carry = A & B;
        A = A ^ B;
        B = carry << 1;
    }
    int check = A & 0xffffffff;
    printf("%d\n", A);
    printf("%d\n", check);
    return 0;
}