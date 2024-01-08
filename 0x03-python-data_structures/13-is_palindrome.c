#include "lists.h"

/* Function prototypes for helper functions */
void reverse_list(listint_t **head);
int compare_lists(listint_t *list1, listint_t *list2);

int is_palindrome(listint_t **head)
{
    listint_t *slow = *head, *fast = *head;
    listint_t *prev_slow = *head;
    listint_t *second_half, *mid_node = NULL;
    int is_palindrome = 1;

    if (*head == NULL || (*head)->next == NULL)
        return 1; // Empty list or single-node list is a palindrome

    // Move 'fast' two steps and 'slow' one step at a time until 'fast' reaches the end
    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;
        prev_slow = slow;
        slow = slow->next;
    }

    // Handle odd number of nodes
    if (fast != NULL)
    {
        mid_node = slow;
        slow = slow->next;
    }

    // Reverse the second half of the linked list
    reverse_list(&second_half);

    // Compare the first half and reversed second half
    is_palindrome = compare_lists(*head, second_half);

    // Restore the original list
    reverse_list(&second_half);
    if (mid_node != NULL)
    {
        prev_slow->next = mid_node;
        mid_node->next = second_half;
    }
    else
    {
        prev_slow->next = second_half;
    }

    return is_palindrome;
}
/**
 * reverse_list - Reverses a linked list.
 * @head: Pointer to the head of the linked list.
 */
void reverse_list(listint_t **head)
{
    listint_t *prev = NULL, *current = *head, *next = NULL;

    while (current != NULL)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    *head = prev;
}

/**
 * compare_lists - Compares two linked lists.
 * @list1: Pointer to the head of the first linked list.
 * @list2: Pointer to the head of the second linked list.
 *
 * Return: 1 if the lists are equal, 0 otherwise.
 */
int compare_lists(listint_t *list1, listint_t *list2)
{
    while (list1 != NULL && list2 != NULL)
    {
        if (list1->n != list2->n)
            return 0;
        list1 = list1->next;
        list2 = list2->next;
    }

    return (list1 == NULL && list2 == NULL);
}
