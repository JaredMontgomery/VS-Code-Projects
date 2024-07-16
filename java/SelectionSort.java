public class SelectionSort
{
    /**
     * Performs selection sort in-place on an array of numbers. It works by
     * repeatedly selecting the smallest number in a portion of the array and
     * moving it to the right.
     * 
     * Time complexity - O(N^2), where N is [arr.length].
     * Space complexity - O(1).
     * 
     * @param arr The number array to sort in-place.
     * 
     * @author Jared Austin Montgomery
     */
    public static <T> void selectionSort(T[] arr)
    {
        // Iterates over the array repeatedly until everything is sorted.
        for (int i = 0; i < arr.length; i++)
        {
            // The index of the biggest number found in an iteration. Used for
            // swapping that number with another later.
            int maxIndex = 0;

            // Iterates over a portion of the array and finds the index of the
            // biggest number in it.
            for (int j = 0; j < arr.length - i; j++)
            {
                if (arr[j] > arr[maxIndex])
                {
                    maxIndex = j;
                }
            }

            // Swaps the biggest number found in a portion with a number at the
            // end.
            int temp = arr[maxIndex];
            arr[maxIndex] = arr[arr.length - 1 - i];
            arr[arr.length - 1 - i] = temp;
        }
    }
}