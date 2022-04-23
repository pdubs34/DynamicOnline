/*             *
 * CODE DRIVER *
 *             */

/*
 * KeyboardLab (c) 2021 Christopher A. Bohn
 */

#include <stdio.h>
#include <ctype.h>

int produce_multiple_of_ten(int seed);
int is_even(int number);

int main() {
    int number;
    printf("Enter a number: ");
    scanf("%d", &number);
    printf("%d", number);
    printf("produce_multiple_of_ten(%d) = %d\n", number, produce_multiple_of_ten(number));
}