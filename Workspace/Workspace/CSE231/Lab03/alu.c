/*
 * STUDENT: (Type your name here)
 */

/*
 * IntegerLab (c) 2018-21 Christopher A. Bohn
 */

/******************************************************************************
 * In this lab, students are required to implement integer arithmetic for
 * unsigned 16-bit integers and signed (twos complement) 16-bit integers using
 * only bitwise and (&), bitwise or (|), bitwise xor (^), bitwise complement
 * (~), and bit shifts (<< and >>). DO NOT USE built-in addition (+),
 * subtraction (-), multiplication (*), division (/), nor modulo (%).
 ******************************************************************************/

#include "alu.h"
#include "stdio.h"

/* Adds the two arguments and stores the sum in the return structure's result
 * field.  If the operation overflowed then the overflow flag is set. */
int findSign(int number){
    number = number & 0x8000;
    if(number){
        return 1;
    }
    return 0;
}
uint32_t adder(uint32_t A, uint32_t B){
    while (B != 0) {
        int carry = A & B;
        A = A ^ B;
        B = carry << 1;
    }
    return A;
}

addition_subtraction_result add(uint16_t augend, uint16_t addend) {
    addition_subtraction_result addition;
    int result = augend;
    int adder = addend;
    while (adder != 0) {
        int carry = result & adder;
        result = result ^ adder;
        adder = carry << 1;
    }
    int check = result & 0xffff;
    if(is_signed){
        int augendSign = findSign(augend);
        int addendSign = findSign(addend);
        int resultSign = findSign(result);
        if(augendSign == addendSign){
            if((resultSign == 1) & (addendSign == 1)){
                addition.overflow = false;
            }
             if((resultSign == 1) & (addendSign == 0)){
                addition.overflow = true;
            }
             if((resultSign == 0) & (addendSign == 0)){
                addition.overflow = false;
            }
             if((resultSign == 0) & (addendSign == 1)){
                addition.overflow = true;
            }
        }
        else{
            addition.overflow = false;
        }
    }
    else{
        if((check < augend) | (check < addend)){
            addition.overflow = true;
        }
        else{
            addition.overflow = false;
        }
    }
    addition.result = check;
    return addition;
}

/* Subtracts the second argument from the first, stores the difference in the
 * return structure's result field.  If the operation overflowed then the
 * overflow flag is set. */
addition_subtraction_result subtract(uint16_t menuend, uint16_t subtrahend) {
    addition_subtraction_result subtract;
    uint16_t augend = menuend;
    uint16_t addend = ~(subtrahend);
    addend = add(addend,1).result;    
    subtract = add(augend, addend);
    if(is_signed == false){
        //this has the exact opposite conditions of unsigned overflow(using < logic) so you flip the overthrow value.
        if(subtract.overflow == true){
            subtract.overflow = false;
        }
        else{
            subtract.overflow = true;
        }   
    }   
    return subtract;
}

/* Multiplies the two arguments.  The function stores lowest 16 bits of the
 * product in the return structure's product field and the full 32-bit product
 * in the full_product field.  If the product doesn't fit in the 16-bit
 * product field then the overflow flag is set. */
multiplication_result multiply(uint16_t multiplicand, uint16_t multiplier) {
    multiplication_result multiplication;
    multiplication.overflow = false;
    uint32_t z = 0;
    uint32_t x = multiplicand;
    uint32_t y = multiplier;
    while(y != 0 && x != 0){
        int multiplierLSB = y & 1;
        if(multiplierLSB == 1){
            z = adder(z,x);
        } 
        y = y >> 1;
        x = x << 1;
        }
    uint16_t product = z;
    multiplication.product = product;
    multiplication.full_product = z;
    if(multiplication.full_product != multiplication.product){
        multiplication.overflow = true;
    }
    return multiplication;
}

/* Divides the first argument by the second.  The function stores the quotient
 * in the return structure's quotient field and the the quotient in the
 * remainder field.  If the divisor is zero then the quotient and remainder
 * fields should be ignored, and the division_by_zero field should be set. */
division_result divide(uint16_t dividend, uint16_t divisor) {
    division_result division;
    division.division_by_zero = true;
    uint32_t x = dividend;
    uint32_t y = divisor;
    int z = 0;
    int i = 0;
    if(y){
        y = y << 16;
        while(i != 17){
            z = z << 1;
            if(x >= y){
                x = subtract(x,y).result;
                z = add(z,1).result;
            }
            y = y >> 1;
            i = add(i,1).result;
        }
        division.quotient = z;
        division.remainder = subtract(dividend,multiply(divisor,z).product).result;
        division.division_by_zero = false;
    } 
    return division;
}