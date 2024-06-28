/*
 * This program takes an array at the command line and sorts the array in-place
 * using bubble sort. The results are then printed out.
 * 
 * @author Jared Austin Montgomery
 */

#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <string>

// Used for error handling to make the text stand out more.
#define RED "\e[0;31m"
#define RESET "\e[0m"

void bubbleSort(int* arr, size_t len, bool ascending);
bool strIsInteger(char* str);

int main(int argc, char** argv)
{
    // Determines if the number used for sorting is a valid int.
    if (strIsInteger(argv[1]) == false)
    {
        return 1;
    }

    // If 0 is passed in, then ascending order isn't used. If anything else is
    // passed in, then ascending order is used.
    bool ascending = argv[1] == "0";

    int* arr = new int[argc - 2];
    size_t len = argc - 2;

    // Iterates over argv and ensures that all strings are valid numbers. Also,
    // adds said numbers to an int array.
    for (int i = 0; i < len; i++)
    {
        if (strIsInteger(argv[i + 2]) == false)
        {
            return 1;
        }

        arr[i] = std::atoi(argv[i + 2]);
    }

    bubbleSort(arr, len, ascending);

    std::printf("Sorted arr: ");
    // Iterates over and prints the resulting sorted array.
    for (int i = 0; i < len; i++)
    {
        std::printf("%i, ", arr[i]);
    }
    std::printf("\b\b.\n");
}

/**
 * Sorts nums in an int array by repeatedly iterating over it and moving the
 * biggest nums to the right on each iteration. By default, sorting will be done
 * in ascending order.
 * 
 * Time complexity - O(N^2), where N is len.
 * Space complexity - O(1).
 * 
 * @param arr The array to sort.
 * @param len The array length.
 * @param ascending The ordering used by the final, sorted array.
 * 
 * @author Jared Austin Montgomery
 */
void bubbleSort(int* arr, size_t len, bool ascending=true)
{
    for (int i = 0; i < len - 1; i++)
    {
        // Used to keep track of whether or not a swap has happened.
        bool swapped = false;

        // Iterates over the array and swaps 2 adjacent numbers if they are in
        // the wrong order.
        for (int j = 0; j < len - 1 - i; j++)
        {
            if (ascending) {
                if (arr[j] > arr[j + 1])
                {
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;

                    swapped = true;
                }

                continue;
            }

            if (arr[j] < arr[j + 1])
            {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;

                swapped = true;
            }
        }

        // If no swaps happened, then the array must be already fully sorted.
        if (swapped == false)
        {
            break;
        }
    }
}

/*
 * An error handling function. If a given string isn't a valid integer, then an
 * error message is printed.
 * 
 * Time complexity - O(N), where N is the length of str.
 * Space complexity - O(1).
 * 
 * @param str The string to check the validity for.
 * 
 * @return true if str is an integer and false otherwise.
 * 
 * @author Jared Austin Montgomery
 */
bool strIsInteger(char* str)
{
    // Iterates over the chars of str.
    for (int i = 0; str[i] != '\0'; i++)
    {
        // If a non-digit char is found, then that's no good. :(
        if (std::isdigit(str[i]) == 0)
        {
            std::printf(
                RED
                "Error: Char '%c' at index %i of string \"%s\" isn't a digit.\n"
                RESET,
                str[i],
                i, str
            );

            return false;
        }
    }

    return true;
}