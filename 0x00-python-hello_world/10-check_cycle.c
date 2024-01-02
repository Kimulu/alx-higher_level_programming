#include <stdio.h>
#include <stdlib.h>

/* Definition for singly-linked list node */
typedef struct listint_s {
    int n;
    struct listint_s *next;
} listint_t;

/* Function to check if a singly linked list has a cycle */
int check_cycle(listint_t *list) {
    listint_t *tortoise = list;
    listint_t *hare = list;

    while (hare != NULL && hare->next != NULL) {
        tortoise = tortoise->next;
        hare = hare->next->next;

        /* If there's a cycle, the tortoise and hare will meet */
        if (tortoise == hare) {
            return 1; /* Cycle detected */
        }
    }

    return 0; /* No cycle */
}
