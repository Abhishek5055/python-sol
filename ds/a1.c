#include <stdio.h>
#include <stdlib.h>  // Add this for the malloc function

typedef struct node
{
    int data;
    struct node *next;  // Corrected this line
} node;

void insertAtBeginning(node **head, int data)
{
    node *newNode = (node *)malloc(sizeof(node));

    newNode->data = data;
    newNode->next = *head;

    *head = newNode;
}

void display(node *head)
{
    while (head != NULL)
    {
        printf("%d ", head->data);  // Corrected this line
        head = head->next;
    }
    printf("\n");  // Add a newline after printing the list
}

int main()  // Changed return type to int
{
    node *head = NULL;
    insertAtBeginning(&head, 7);
    insertAtBeginning(&head, 10);
    display(head);  // Corrected this line
    return 0;  // Added return statement
}