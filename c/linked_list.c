#include <stdio.h>
#include <stdlib.h>

// A node for a singly-linked list.
typedef struct ListNode
{
    int num;

    struct ListNode* prev;
    struct ListNode* next;
}
ListNode;

// A struct for a singly-linked list. Has a head and a tail that can be inserted
// at.
typedef struct LinkedList
{
    ListNode* head;
    ListNode* tail;

    // The number of nodes in the list.
    int len;

    void (*insert_at_head)(struct LinkedList* list, int num);
    void (*insert_at_tail)(struct LinkedList* list, int num);

    int (*remove_at_head)(struct LinkedList* list);
    int (*remove_at_tail)(struct LinkedList* list);
}
LinkedList;

// This inserts a node with a value of [num] at the head of a linked list.
void insert_at_head(LinkedList* list, int num)
{
    ListNode* new_node = malloc(sizeof(ListNode));
    new_node->num = num;
    new_node->prev = NULL;
    // The new node points to the head.
    new_node->next = list->head;

    // The new node becomes the new head.
    list->head = new_node;

    list->len++;
}

// This removes a node with a value at the head of a linked list and returns its
// value.
int remove_at_head(LinkedList* list)
{
    // Can't remove what isn't there.
    if (list->len == 0)
    {
        return 0;
    }

    int old_num = list->head->num;

    // Advances the head forwards.
    list->head = list->head->next;

    // Deletes the old head.
    free(list->head->prev);

    list->len--;

    return old_num;
}

// This inserts a node with a value of [num] at the tail of a linked list.
void insert_at_tail(LinkedList* list, int num)
{
    ListNode* new_node = malloc(sizeof(ListNode));
    new_node->num = num;
    // The new node goes after the tail.
    new_node->prev = list->tail;
    new_node->next = NULL;

    list->tail->next = new_node;
    // The new node becomes the new tail.
    list->tail = new_node;

    list->len++;
}

// This removes a node with a value at the tail of a linked list and returns its
// value.
int remove_at_tail(LinkedList* list)
{
    // Can't remove what isn't there.
    if (list->len == 0)
    {
        return 0;
    }

    int old_num = list->tail->num;

    // Advances the tail backwards.
    list->tail = list->tail->prev;

    // Deletes the old tail.
    free(list->tail->next);

    list->len--;

    return old_num;
}

int main(void)
{
    // Creates a list and sets some stuff up:

    LinkedList* list = malloc(sizeof(LinkedList));

    list->insert_at_head = insert_at_head;
    list->insert_at_tail = insert_at_tail;

    list->remove_at_head = remove_at_head;
    list->remove_at_tail = remove_at_tail;

    // Creates the head node.
    list->head = malloc(sizeof(ListNode));
    list->head->num = 1;
    list->head->next = NULL;

    list->len = 1;

    // Only 1 node for now, so the head and the tail are the same.
    list->tail = list->head;

    list->insert_at_tail(list, 1);
    list->insert_at_tail(list, 2);
    list->insert_at_tail(list, 3);
    list->insert_at_tail(list, 4);

    printf("%d", list->remove_at_head(list));

    // ListNode* node = list->head;

    // // Iterates over the list.
    // while (node != NULL)
    // {
    //     printf("%d\n", node->num);

    //     node = node->next;
    // }
}