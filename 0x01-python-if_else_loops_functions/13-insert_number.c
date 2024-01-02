#include <stdlib.h>

/* Define the structure for a singly linked list node */
typedef struct listint_s {
    int n;
    struct listint_s *next;
} listint_t;

/* Function to insert a number into a sorted linked list */
listint_t *insert_node(listint_t **head, int number) {
    listint_t *new_node, *current, *prev;

    /* Allocate memory for the new node */
    new_node = malloc(sizeof(listint_t));
    if (new_node == NULL) {
        return NULL;  /* Memory allocation failed */
    }

    /* Set the value of the new node */
    new_node->n = number;
    new_node->next = NULL;

    /* Check if the list is empty or the new node should be inserted at the beginning */
    if (*head == NULL || number < (*head)->n) {
        new_node->next = *head;
        *head = new_node;
        return new_node;
    }

    /* Traverse the list to find the correct position to insert the new node */
    current = *head;
    prev = NULL;
    while (current != NULL && current->n < number) {
        prev = current;
        current = current->next;
    }

    /* Insert the new node at the correct position */
    prev->next = new_node;
    new_node->next = current;

    return new_node;
}

