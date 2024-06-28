public class SelectionSort
{
    public static void main(String[] args)
    {
        int[] arr = {4, 3, 2, 1};

        arr = selectionSort(arr);

        for (int n : arr)
        {
            System.out.print(n + ", ");
        }
    }

    public static int[] selectionSort(int[] arr)
    {
        for (int i = 0; i < arr.length - 1; i++)
        {
            int max = Integer.MIN_VALUE;
            int maxIndex = 0;

            for (int j = i; j < arr.length - 1; j++)
            {
                if (arr[j] > max)
                {
                    max = arr[j];
                    maxIndex = j;
                }
            }

            int temp = arr[maxIndex];
            arr[maxIndex] = arr[arr.length - 1 - i];
            arr[arr.length - 1 - i] = temp;
        }

        return arr;
    }
}