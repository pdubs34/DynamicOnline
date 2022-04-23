/*
 * STUDENT: (Type your name here)
 */

/*
 * KeyboardLab (c) 2021 Christopher A. Bohn
 */

/******************************************************************************
 * This code will implement functions equivalent to ctype.h's isdigit() and
 * tolower() without #include'ing any files, without using any number keys
 * other than 0 and 9 (and 7, which has the & symbol), without using any switch
 * statements, and using at most one if statement in each function.
 ******************************************************************************/

/* Returns 1 if the argument is a decimal digit (such as '5'), 0 otherwise */

#include <stdio.h>

int is_digit(char character) {
    if(character >= '0' && character <= '9'){
        return 1;
    }
    return 0;
}

/* Converts uppercase letters to lowercase letters.
 * If the argument is an uppercase letter, the function returns the
 * corresponding lowercase letter (e.g., 'D' yields 'd'). Otherwise, the
 * function returns the argument, unchanged. */
char to_lowercase(char character) {
    int add = ' ';
    if(character >= 'A' && character <= 90){
        return character + add;
    }
    return character;
}