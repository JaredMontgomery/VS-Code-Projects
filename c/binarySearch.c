/*
This program uses binary search to find and print the index for a number in an
array (if it can be found). Both the target number and the array are passed as
command line arguments with the number coming first.

Time complexity - O(log(N)), where N is the length of the array.
Space complexity - O(N).

@author Jared Austin Montgomery
*/

#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>

// Used for error handling to make the text stand out more.
#define RED "\e[0;31m"
#define RESET "\e[0m"

unsigned int iterativeBinarySearch(int* arr, size_t len, int num);
unsigned int recursiveBinarySearch(int* arr, size_t len, int num, unsigned int lower, unsigned int upper);
short strIsInteger(char* str);

int main(int argc, char** argv)
{
    // Ensures that the number for the algo chosen and the target number are
    // valid integers.
    if (strIsInteger(argv[1]) == 0 || strIsInteger(argv[2]) == 0)
    {
        return 1;
    }

    short algoChoice = atoi(argv[1]);

    // Ensures that the algoChoice num is in the appropriate range. 1 for
    // iterative binary search and 2 for recursive.
    if (algoChoice < 1 || algoChoice > 2)
    {
        printf(
            RED
            "Error: %i for algoChoice isn't 1 or 2.\n"
            RESET,
            algoChoice
        );

        return 1;
    }

    // The number to find in the array.
    int num = atoi(argv[2]);

    // The aforementioned array.
    int* arr = malloc((argc - 3) * sizeof(int));
    size_t len = argc - 3;

    // Iterates over argv and ensures that all strings are valid numbers. Also,
    // adds said numbers to an int array.
    for (int i = 0; i < len; i++)
    {
        if (strIsInteger(argv[i + 3]) == 0)
        {
            return 1;
        }

        arr[i] = atoi(argv[i + 3]);
    }

    if (algoChoice == 1)
    {
        printf("iterativeBinarySearch():\n");
        printf("Found %i at index %i.\n", num, iterativeBinarySearch(arr, len, num));
        
        return 0;
    }

    printf("recursiveBinarySearch():\n");
    printf("Found %i at index %i.\n", num, recursiveBinarySearch(arr, len, num, 0, len - 1));
}

/*
Binary search using an iterative approach. It works by looking at the center of
a (sorted) array for the target number. If found, its index is returned.
Otherwise, the other portion of the array that could contain the number is
searched.

Time complexity - O(log(N)), where N is len.
Space complexity - O(1).

@param arr The int array to search over.
@param len The length of the array.
@param num The number to look for.

@return The index of the number if found and -1 otherwise.

@author Jared Austin Montgomery
*/
unsigned int iterativeBinarySearch(int* arr, size_t len, int num)
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
Binary search using a recursive approach. It works by looking at the center of
a (sorted) array for the target number. If found, its index is returned.
Otherwise, the other portion of the array that could contain the number is
searched.

Time complexity - O(log(N)), where N is len.
Space complexity - O(1).

@param arr The int array to search over.
@param len The length of the array.
@param num The number to look for.
@param lower The lower bound of the current arr portion of interest.
@param upper The upper bound of the current arr portion of interest.

@return The index of the number if found and -1 otherwise.

@author Jared Austin Montgomery
*/
unsigned int recursiveBinarySearch(int* arr, size_t len, int num, unsigned int lower, unsigned int upper)
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
        return recursiveBinarySearch(arr, len, num, lower, middle - 1);
    }
    // If num is after middle, then increase lower bound.
    else if (num > arr[middle])
    {
        return recursiveBinarySearch(arr, len, num, middle + 1, upper);
    }
}

/*
An error handling function. If a given string isn't a valid integer, then an
error message is printed.

Time complexity - O(N), where N is the length of str.
Space complexity - O(1).

@param str The string to check the validity for.

@return true if str is an integer and false otherwise.

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