/**
 * This program is an attempt at implementing an array... It's very basic, but
 * that's because arrays are already very basic.
 */

#include <stdio.h>
#include <stdlib.h>

/**
 * Creates and returns n array of a certain length.
 * 
 * Time complexity - O(N), where N is [len].
 * Space complexity - O(N).
 */
int* Array(size_t len)
{
    return malloc(len * sizeof(int));
}

/**
 * Gets and returns an int at an index in an array.
 * 
 * Time complexity - O(1).
 * Space complexity - O(1).
 */
int get(int* arr, size_t index)
{
    return arr[index];
}

/**
 * Sets an int at an index in an array. The new int is returned.
 * 
 * Time complexity - O(1).
 * Space complexity - O(1).
 */
int set(int* arr, size_t index, int item)
{
    return arr[index] = item;
}

/**
 * Inserts an int at an index in an array. The new int is returned. Items are
 * shifted over to the right and any item at the end of the array is discarded.
 * 
 * Time complexity - O(N), where N is [len].
 * Space complexity - O(1).
 */
int insert(int* arr, size_t index, size_t len, int item)
{
    // Shifts items at the index to the right.
    for (int i = len - 1; i > index; i--)
    {
        arr[i] = arr[i - 1];
    }

    arr[index] = item;

    return item;
}

/**
 * Deletes an int at an index in an array. The removed int is returned. Items
 * are shifted over to the left. The last item in the array will be empty (0).
 * 
 * Time complexity - O(N), where N is [len].
 * Space complexity - O(1).
 */
int delete(int* arr, size_t index, size_t len)
{
    // Item that's getting removed.
    int item = arr[index];

    // Shifts items at the index to the left.
    for (int i = index; i < len - 1; i++)
    {
        arr[i] = arr[i + 1];
    }

    arr[len - 1] = 0;

    return item;
}

/**
 * Tests the above functions by making an array, adding stuff, then printing.
 */
int main(void)
{
    // Creates an array.
    int len = 4;
    int* arr = Array(len);
    
    // Adds items.
    for (size_t i = 0; i < len; i++)
    {
        set(arr, i, i + 1);
    }

    // Prints items.
    for (size_t i = 0; i < len; i++)
    {
        printf("%d\n", get(arr, i));
    }
    printf("\n");

    insert(arr, 0, len, 10);

    // Prints items to see the insertion.
    for (size_t i = 0; i < len; i++)
    {
        printf("%d\n", get(arr, i));
    }
    printf("\n");

    delete(arr, 0, len);

    // Prints items to see the deletion.
    for (size_t i = 0; i < len; i++)
    {
        printf("%d\n", get(arr, i));
    }
    printf("\n");
}