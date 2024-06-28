#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>

void quickSort(int* arr, size_t len);
void quickSortAlgo(int* arr, int start, int end);
int partition(int* arr, int left, int right, int pivot);

/*
 * Tests out the implementation of quick sort by letting the user enter numbers for
 * the array. The results are later printed out.
 * 
 * Time complexity - O(N^2), where N is argc - 1.
 * Space complexity - O(N), where N is argc - 1.
 */
int main(int argc, char **argv)
{
    // Creates and sets up an array that can store all of the numbers that the
    // user entered.
    int* arr = malloc(sizeof(int) * (argc - 1));

    // Iterates over each argument.
    for (int i = 1; i < argc; i++)
    {
        // Ensures that an arg is actually a number by iterating over its chars
        // and checking for non-digit chars.
        for (int j = 0; argv[i][j] != '\0'; j++)
        {
            if (isdigit(argv[i][j]) == 0)
            {
                printf("Error: Argument \"%s\" is not a number.\n", argv[i]);
                return 1;
            }
        }

        arr[i - 1] = atoi(argv[i]);
    }

    quickSort(arr, argc - 1);

    // Prints out the whole array on one line:

    printf("Results: ");

    for (int i = 0; i < argc - 1; i++)
    {
        printf("%i, ", arr[i]);
    }

    printf("\b\b.");
}

/*
 * Runs the quick sort algorithm by using a longer function with more arguments.
 * This is done so that you can use quickSort() without having to plug in many
 * arguments.
 * 
 * @param arr A pointer to an int array to sort in ascending order.
 * @param len The number of items in said array.
 */
void quickSort(int* arr, size_t len)
{
    quickSortAlgo(arr, 0, len - 1);
}

/*
 * Actually runs the quick sort algorithm on an array (arr) of a certain size (len)
 * from one index (start) to another (end). Recursion is used to sort the smaller
 * subarrays.
 * 
 * Time complexity - O(N^2), where N is len.
 * Space complexity - O(1).
 * 
 * @param arr A pointer to an int array to sort in ascending order.
 * @param start The starting index.
 * @param end The ending index.
 */
void quickSortAlgo(int* arr, int start, int end)
{
    if (start < end)
    {
        // Gets the item in the middle of the subarray. Numbers in the array
        // will pivot around (swapped around) this number.
        int pivot = arr[(start + end) / 2];

        // After numbers are swapped around a pivot, a new index is given and
        // the algorithm is run 2 smaller subarrays. The first goes from start
        // to index and the second goes from index + 1 to end.
        int index = partition(arr, start, end, pivot);

        quickSortAlgo(arr, start, index - 1);
        quickSortAlgo(arr, index, end);
    }
}

/*
 * Takes a part of an array (arr) and swaps numbers around a pivot number using
 * "pointers".
 * 
 * Time complexity - O(N), where N is right - left.
 * Space complexity - O(1).
 * 
 * @param arr A pointer to an int array to sort in ascending order.
 * @param left The index of the "pointer" on the left.
 * @param right The index of the "pointer" on the right.
 * @param pivot The number to swap other numbers around.
*/
int partition(int* arr, int left, int right, int pivot)
{
    // There are 2 "pointers" here. Each one (left and right) holds a different
    // index. Each index will move into the subarray until a number is found
    // that doesn't belong in that half of the subarray. The loop ends when they
    // cross over each other.
    while (left <= right)
    {
        // Goes until a number too big is found.
        while (arr[left] < pivot)
        {
            left++;
        }

        // Goes until a number too small is found.
        while (arr[right] > pivot)
        {
            right--;
        }

        if (left <= right)
        {
            // Swaps each number around, rotating them around the pivot.
            int temp = arr[left];
            arr[left] = arr[right];
            arr[right] = temp;

            left++;
            right--;
        }
    }

    return left;
}

/*
 * Algorithm:
 * 
 * 1. Take an array and choose the number in the middle. This is the pivot. Other
 * items are going to rotate around it.
 * 
 * 2. Make 2 variables. We'll call them start and end. These will hold indices
 * from the array with left starting at 0 and right holding the last index.
 * 
 * 3. Make 2 pointers. We'll call them left and right. left and right will be set
 * to start and end.
 * 
 * 4. Increase left until a number is found that is greater than the pivot.
 * 
 * 5. Decrease rightt until a number is found that is less than the pivot.
 * 
 * 6. Swap the numbers pointed to by each pointer.
 * 
 * 7. Once left surpasses right, then continue on. Otherwise, go back to step 3.
 * 
 * 8. Take left and assign it to another variable. We'll call it index.
 * 
 * 9. Now, run the algorithm again from the indices start to index. Then, run it
 * again from the indices index + 1 and end.
 */