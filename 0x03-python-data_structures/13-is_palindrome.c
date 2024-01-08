#include <stdio.h>
#include <stdlib.h>

typedef struct listint {
    int n;
    struct listint *next;
} listint_t;

int is_palindrome(listint_t **head);

int main(void)
{
    listint_t *head, *node1, *node2, *node3, *node4, *node5;

    node5 = malloc(sizeof(listint_t));
    node5->n = 1;
    node5->next = NULL;

    node4 = malloc(sizeof(listint_t));
    node4->n = 2;
    node4->next = node5;

    node3 = malloc(sizeof(listint_t));
    node3->n = 3;
    node3->next = node4;

    node2 = malloc(sizeof(listint_t));
    node2->n = 2;
    node2->next = node3;

    node1 = malloc(sizeof(listint_t));
    node1->n = 1;
    node1->next = node2;

    head = node1;

    if (is_palindrome(&head))
        printf("The linked list is a palindrome\n");
    else
        printf("The linked list is not a palindrome\n");

    // Free the allocated memory
    while (head)
    {
        listint_t *temp = head;
        head = head->next;
        free(temp);
    }

    return (0);
}

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
    second_half = slow;
    prev_slow->next = NULL; // Break the link to the first half
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

void reverse_list(listint_t **head)
{
    listint_t *prev = NULL;
    listint_t *current = *head;
    listint_t *next = NULL;

    while (current != NULL)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    *head = prev;
}

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

