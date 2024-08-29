/**
 * This program is an attempt at implementing an array... It's very basic, but
 * that's because arrays are already very basic.
 */

#include <stdio.h>
#include <stdlib.h>

/**
 * Creates and returns n array of a certain size.
 * 
 * Time complexity - O(N).
 * Space complexity - O(N).
 */
int* Array(size_t size)
{
    return malloc(size * sizeof(int));
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
 * Tests the above functions by making an array, adding stuff, then printing.
 */
int main(void)
{
    int* arr = Array(4);
    
    for (size_t i = 0; i < 4; i++)
    {
        set(arr, i, i + 1);
    }

    for (size_t i = 0; i < 4; i++)
    {
        printf("%d\n", get(arr, i));
    }
}