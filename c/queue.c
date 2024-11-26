#include <stdio.h>
#include <stdlib.h>

// A node for a singly-linked list.
typedef struct ListNode
{
    int num;
    struct ListNode* next;
}
ListNode;

// A struct for a singly-linked list. Has a head and a tail that can be inserted
// at.
typedef struct LinkedList
{
    ListNode* head;
    ListNode* tail;

    void (*insert_at_head)(struct LinkedList* list, int num);
    void (*insert_at_tail)(struct LinkedList* list, int num);
}
LinkedList;

// This inserts a node with a value of [num] at the head of a linked list.
void insert_at_head(LinkedList* list, int num)
{
    ListNode* new_node = malloc(sizeof(ListNode));
    new_node->num = num;
    new_node->next = NULL;

    // The new node points to the head and becomes the new head.
    new_node->next = list->head;
    list->head = new_node;
}

// This inserts a node with a value of [num] at the tail of a linked list.
void insert_at_tail(LinkedList* list, int num)
{
    ListNode* new_node = malloc(sizeof(ListNode));
    new_node->num = num;
    new_node->next = NULL;

    // The new node goes after the tail and becomes the new tail.
    list->tail->next = new_node;
    list->tail = new_node;
}

int main(void)
{
    // Creates a list and sets some stuff up.
    LinkedList* list = malloc(sizeof(LinkedList));
    list->insert_at_head = insert_at_head;
    list->insert_at_tail = insert_at_tail;

    // Creates the head node.
    list->head = malloc(sizeof(ListNode));
    list->head->num = 1;
    list->head->next = NULL;

    // Only 1 node for now, so the head and the tail are the same.
    list->tail = list->head;

    list->insert_at_tail(list, 2);
    list->insert_at_head(list, 3);
    list->insert_at_tail(list, 4);

    ListNode* node = list->head;

    // Iterates over the list.
    while (node != NULL)
    {
        printf("%d\n", node->num);

        node = node->next;
    }
}