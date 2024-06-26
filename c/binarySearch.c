#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>

// Used for error handling to make the text stand out more.
#define RED "\e[0;31m"
#define RESET "\e[0m"

unsigned int binarySearch(int* arr, size_t len, int num);
short strIsInteger(char* str);

int main(int argc, char** argv)
{
    if (strIsInteger(argv[1]) == 0)
    {
        return 1;
    }

    // The number to find in the array.
    int num = atoi(argv[1]);

    // The mentioned array. 
    int* arr = malloc((argc - 2) * sizeof(int));
    size_t len = argc - 2;

    // Iterates over argv and ensures that all strings are valid numbers. Also,
    // adds said numbers to an int array.
    for (int i = 0; i < len; i++)
    {
        if (strIsInteger(argv[i + 2]) == 0)
        {
            return 1;
        }

        arr[i] = atoi(argv[i + 2]);
    }

    printf("binarySearch():\n");
    printf("Found %i at index %i.\n", num, binarySearch(arr, len, num));
}

/*
Binary search using an iterative approach. It works by looking at the center of
a (sorted) array for the target number. If found, its index is returned.
Otherwise, the other portion of the array that could contain the number is
searched.

Time complexity - log(N), where N is len.
Space complexity - O(1).

@param arr The int array to search over.
@param len The length of the array.
@param num The number to look for.

@return The index of the number if found and -1 otherwise.

@author Jared Austin Montgomery
*/
unsigned int binarySearch(int* arr, size_t len, int num)
{
    // Lower and upper indices / bounds of the array portion of interest.
    unsigned int lower = 0;
    unsigned int upper = len - 1;

    while (1)
    {
        unsigned int middle = (lower + upper) / 2;

        if (arr[middle] == num)
        {
            return middle;
        }
        // If num isn't in the middle of the portion and the portion has size 1,
        // then the num isn't in the array.
        else if (lower >= upper)
        {
            return -1;
        }
        // If num is before middle, then reduce upper bound.
        else if (num < arr[middle])
        {
            upper = middle - 1;
        }
        // If num is after middle, then increase lower bound.
        else if (num > arr[middle])
        {
            lower = middle + 1;
        }
    }
}

/*
An error handling function. If a given string isn't a valid integer, then an
error message is printed.

Time complexity - O(N), where N is the length of str.
Space complexity - O(1).

@param str The string to check the validity for.

@return 1 (true) if str is an integer and 0 (false) otherwise.

@author Jared Austin Montgomery
*/
short strIsInteger(char* str)
{
    // Iterates over the chars of str.
    for (int i = 0; str[i] != '\0'; i++)
    {
        // If a non-digit char is found, then that's no good. :(
        if (isdigit(str[i]) == 0)
        {
            printf(
                RED
                "Error: Char '%c' at index %i of string \"%s\" isn't a digit.\n"
                RESET,
                str[i],
                i, str
            );

            return 0;
        }
    }

    return 1;
}