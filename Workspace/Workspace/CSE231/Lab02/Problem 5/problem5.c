/*
 * STUDENT: Payton Webb
 */

/*
 * KeyboardLab (c) 2021 Christopher A. Bohn
 */

/******************************************************************************
 * This program will implement the Pleistocene Petting Zoo's
 * challenge-and-response system.
 ******************************************************************************/

#include <stdio.h>
#include <stddef.h>
#include <stdlib.h>
#include <string.h>

#define MAXIMUM_WORD_LENGTH 60

char to_lowercase(char character);      // linked from problem2.c
int is_even(int number);                // linked from problem3.c
struct node *create_node(const char *word);
void insert_after(struct node *existing_node, struct node *new_node);
void insert_before(struct node *existing_node, struct node *new_node);
char *word_to_lowercase(const char *word);
int compare_words(const char *word1, const char *word2);
struct node *insert_word(struct node *head, const char *word);
struct node *build_list();
char *respond(const struct node *list, const char *challenge_word);
char *get_input(const char *prompt);


/*** PROBLEM 5.1: Doubly-Linked List ***/

struct node {
    char word[MAXIMUM_WORD_LENGTH];
    int occurrences;
    struct node *next;
    struct node *previous;
};

/* Allocates memory for a new node to hold the word, and initializes the node's fields.
 * Returns a pointer to the new node. */
struct node *create_node(const char *word) {
    struct node *new_node = malloc(sizeof(struct node));
    strcpy(new_node -> word,word);
    new_node -> occurrences = 1;
    new_node -> next = NULL;
    new_node -> previous = NULL;
    return new_node;
}

/* Inserts new_node into the list after existing_node; that is, new_node
 * becomes existing_node's "next". If existing_node's original "next" is
 * non-NULL, then that will become new_node's "next". */
void insert_after(struct node *existing_node, struct node *new_node) {
    if(existing_node->next == NULL){
        existing_node->next = new_node;
        new_node->previous = existing_node;
    }
    else{
        struct node *temp = existing_node -> next;
        temp -> previous = new_node;
        new_node->previous = existing_node;
        new_node->next = temp;
        existing_node ->next = new_node;
    }
}

void print_list(const struct node *head) {
    const struct node *current_node;
    current_node = head;
    while (current_node != NULL) {
        printf("NODE %p -- %15s:%d\tprev:%p next:%p\n",
               current_node, current_node->word, current_node->occurrences, current_node->previous, current_node->next);
        current_node = current_node->next;
    }
}
/* Inserts new_node into the list before existing_node; that is, new_node
 * becomes existing_node's "previous". If existing_node's original "previous"
 * is non-NULL, then that will become new_node's "previous". */
void insert_before(struct node *existing_node, struct node *new_node) {
    if(existing_node -> previous == NULL){
        existing_node -> previous = new_node;
        new_node -> next = existing_node;
    }
    else{
        struct node *temp = existing_node->previous;
        temp -> next = new_node;
        new_node -> previous = temp;
        new_node -> next = existing_node;
        existing_node->previous = new_node;
    }
}


/*** PROBLEM 5.2: Alphabetize Words ***/

/* Returns a copy of the word that has all uppercase letters replaced with
 * lowercase letters. The original string is unchanged. */
char *word_to_lowercase(const char *word) {
    int size = strlen(word);
    char *lowercaseWord = (char*)malloc(sizeof(char) * MAXIMUM_WORD_LENGTH);
    for(int i = 0; i < size; i++){
        char c = to_lowercase(word[i]);
        lowercaseWord[i] = c;
    }
    return lowercaseWord;
}

/* Compares two words based on alphabetical order.
 * If word1 occurs alphabetically before word2, then this function returns a negative value.
 * If word1 occurs alphabetically after word2, then this function returns a positive value.
 * If the two words are identical, then this function returns 0.
 * This function is really just a wrapper around strncmp.  */
int compare_words(const char *word1, const char *word2) {
    return strncmp(word1, word2, MAXIMUM_WORD_LENGTH);
}


/*** PROBLEM 5.3: Insertion Sort ***/

/* Determines if the word is already in the list. If it is, then the number of
 * occurrences for that word is incremented. If it isn't, then a new node is
 * created for the word and inserted into the list at the correct alphabetic
 * location. Returns a pointer to the head of the list, which is either the
 * original head or a node containing the word (if the word occurs before the
 * original head's word or if the original head is NULL). */
struct node *insert_word(struct node *head, const char *word) {
    char *copy = (char*)malloc(sizeof(char) * MAXIMUM_WORD_LENGTH);
    strcpy(copy,word_to_lowercase(word));
    if(head == NULL){
        struct node *A = create_node(word);
        return A;
    }
    struct node *current_node = head;
    while (current_node != NULL) {
        if (compare_words(current_node-> word, copy) == 0){
            current_node -> occurrences = (current_node -> occurrences) + 1;
        }
        else if (compare_words(copy, current_node -> word) < 0){
            struct node *A = create_node(copy);
            insert_before(current_node,A);
            break;
        }
        else{
            if(current_node ->next == NULL){
                struct node *A = create_node(copy);
                insert_after(current_node,A);
                break;
            }
        }
        current_node = current_node -> next;
    }
    return head;
}

/* Gets the name of the book file from the user and reads the file line-by-line.
 * Under the assumption that there is exactly one word per line and that all
 * punctuation has been removed, this function builds a doubly-linked list
 * of the words in alphabetical order, keeping track (as part of a node's
 * payload) how many times each word occurs in the file. */
struct node *build_list() {
    const char *filename = get_input("Enter the name of the book file");
    FILE *inputfile = fopen(filename,"r");
    char str[MAXIMUM_WORD_LENGTH];
    struct node *head = insert_word(NULL,str);
    while (fgets(str,MAXIMUM_WORD_LENGTH,inputfile) != NULL){
        head = insert_word(head,str);
    }
    fclose(inputfile);
    return head;
}


/*** PROBLEM 5.4: Respond to Challenge ***/

/* Given an alphabetically sorted list of words with the number of occurrences
 * of each word, and given the challenge_word, will return the response word
 * based on the following rules:
 * - If the number of occurrences is an even number then the response word is
 *   that many places *before* challenge_word in the list
 *   - If the challenge_word is fewer than that number of places from the head
 *     of the list, then the response word is the word at the head of the list
 * - If the number of occurrences is an odd number then the response word is
 *   that many places *after* challenge_word in the list
 *   - If the challenge_word is fewer than that number of places from the tail
 *     of the list, then the response word is the word at the tail of the list
 * - If challenge_word is not present in the list, then the response is
 *   "<challenge_word> is not present!" */
char *respond(const struct node *list, const char *challenge_word) {
    const struct node *current_node;
    current_node = list;
    char *solution = (char*)malloc(sizeof(char) * MAXIMUM_WORD_LENGTH);
    while (current_node != NULL) {
        if(compare_words(challenge_word,current_node->word) == 0){
            if(is_even(current_node -> occurrences) == 1){
                for (int i = 0;i < current_node->occurrences;i++){
                    if(current_node->previous == NULL){
                        solution = current_node->word;
                        return solution;
                    }
                    current_node = current_node -> previous;
                }
                solution = current_node->word;
                return solution;
            }
            if(is_even(current_node->occurrences) == 0){
                for (int i = 0;i < current_node->occurrences;i++){
                    if(current_node->next == NULL){
                        solution = current_node->word;
                        return solution;
                    }
                current_node = current_node ->next;
                }
            solution = current_node->word;
            return solution;
        }
        }
    current_node = current_node->next;
    }
    printf("Could not find %s in list\n",challenge_word);
    return NULL;
}


/*** main ***/

/* A utility function to help with debugging.  Traverses the list, printing
 * each node's payload and the next/previous pointers. */


/* Prompts the user and reads the user's input from stdin. */
char *get_input(const char *prompt) {
    char *input = malloc(MAXIMUM_WORD_LENGTH);
    printf("%s: ", prompt);
    fgets(input, MAXIMUM_WORD_LENGTH, stdin);
    input[strlen(input) - 1] = '\0';        // eliminates the undesired newline character
    return input;
}

int main() {
    // struct node *list = build_list();
    // print_list(list);
    char *challenge_word = get_input("Enter the challenge word");
    struct node *B = create_node("bike");
    struct node *C = create_node("car");
    struct node *D = create_node("dog");
    struct node *E = create_node("eagle");
    struct node *F = create_node("falcon");
    insert_before(C,B);
    insert_after(C,D);
    insert_before(E,D);
    insert_after(E,F);
    if(respond(B, challenge_word) != NULL){
        printf("Response word: %s\n", respond(B, challenge_word));
    }
    //NOTE
    //My buildList and wordToLowercase function both work but my insert_word does not.
    //I couldn't figure out what the issue was.
    return 0;

}
