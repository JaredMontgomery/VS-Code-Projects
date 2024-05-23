#include <stdio.h>
#include <stdlib.h>

void quickSort(int* arr, size_t len);
void quickSortAlgo(int* arr, size_t len, int start, int end);
int partition(int* arr, int left, int right, int pivot);

/*
Tests out the implementation of quick sort by letting the user enter numbers for
the array. The results are later printed out.
*/
int main(int argc, char **argv)
{
    // Creates and sets up an array that can store all of the numbers that the
    // user entered.
    int* arr = malloc(sizeof(int) * (argc - 1));
    for (int i = 0; i < argc - 1; i++)
    {
        arr[i] = atoi(argv[i + 1]);
    }

    quickSort(arr, argc - 1);

    // Prints out the whole array on one line.
    printf("arr: ");
    for (int i = 0; i < argc - 1; i++)
    {
        printf("%i, ", arr[i]);
    }
    printf("\b\b.");
}

/*
Runs the quick sort algorithm by using a longer function with more arguments.
This is done so that you can use quickSort() without having to plug in many
arguments.

@param arr A pointer to an int array to sort in ascending order.
@param len The number of items in said array.
*/
void quickSort(int* arr, size_t len)
{
    quickSortAlgo(arr, len, 0, len - 1);
}

/*
Actually runs the quick sort algorithm on an array (arr) of a certain size (len)
from one index (start) to another (end). Recursion is used to sort the smaller
subarrays.

@param arr A pointer to an int array to sort in ascending order.
@param len The number of items in said array.
@param start The starting index.
@param end The ending index.
*/
void quickSortAlgo(int* arr, size_t len, int start, int end)
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

        quickSortAlgo(arr, len, start, index);
        quickSortAlgo(arr, len, index + 1, end);
    }
}

/*
Takes a part of an array (arr) and swaps numbers around a pivot number using
"pointers".

Time complexity - O(N), where N is right - left.
Space complexity - O(1).

@param arr A pointer to an int array to sort in ascending order.
@param left The index of the "pointer" on the left.
@param right The index of the "pointer" on the right.
@param pivot The number to swap other numbers around.
*/
int partition(int* arr, int left, int right, int pivot)
{
    // There are 2 "pointers" here. Each one (left and right) holds a different
    // index. Each index will move into the subarray until a number is found
    // that doesn't belong in that half of the subarray. The loop ends when they
    // cross over each other.
    while (left < right)
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

        if (left < right)
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
Algorithm:

1. Take an array and choose the number in the middle. This is the pivot. Other
items are going to rotate around it.

1.5. Make 2 variables. We'll call them start and end. These will hold indices
from the array with left starting at 0 and right holding the last index.

2. Make 2 pointers. We'll call them left and right. left and right will be set
to start and end.

3. Increase left until a number is found that is greater than the pivot.

4. Decrease rightt until a number is found that is less than the pivot.

5. Swap the numbers pointed to by each pointer.

6. Once left surpasses right, then continue on. Otherwise, go back to step 3.

7. Take left and assign it to another variable. We'll call it index.

8. Now, run the algorithm again from the indices start to index. Then, run it
again from the indices index + 1 and end.
*/