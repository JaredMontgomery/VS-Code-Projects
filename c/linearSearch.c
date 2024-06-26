#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>

// Used for error handling to make the text stand out more.
#define RED "\e[0;31m"
#define RESET "\e[0m"

unsigned int linearSearch(int* arr, size_t len, int num);
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

    printf("linearSearch():\n");
    printf("Found %i at index %i.\n", num, linearSearch(arr, len, num));
}

/*
Linear search. It simply starts at the beginning of an array and checks every
index for a given number in order.

Time complexity - O(N), where N is len.
Space complexity - O(1).

@param arr The int array to search over.
@param len The length of the array.
@param num The number to look for.

@return The index of the number if found and -1 otherwise.

@author Jared Austin Montgomery
*/
unsigned int linearSearch(int* arr, size_t len, int num)
{
    // Iterates over arr, looking for num.
    for (int i = 0; i < len; i++)
    {
        if (arr[i] == num)
        {
            return i;
        }
    }

    return -1;
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
        // If a non-digit char is found, then that's bad. :(
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