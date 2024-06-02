public class Factorial
{
    /// <summary>
    /// Tests the factorial functions on numbers from 0 to 20.
    /// </summary>
    static void Main(string[] args)
    {
        Console.WriteLine("Factorials using RecursiveFact():");
        // Prints factorials from 0 to 10.
        for (ulong n = 0; n <= 10; n++)
        {
            Console.WriteLine("    {0}! = {1}.", n, RecursiveFact(n));
        }

        Console.WriteLine("Factorials using IterativeFact():");
        // Prints factorials from 11 to 20.
        for (ulong n = 11; n <= 20; n++)
        {
            Console.WriteLine("    {0}! = {1}.", n, IterativeFact(n));
        }
    }

    /// <summary>
    ///     Computes a factorial using iteration.
    /// <br />
    /// <br />
    ///     Time complexity - O(N), where N is num.
    /// <br />
    ///     Space complexity - O(1).
    /// </summary>
    ///
    /// <param name="num"> The input number. </param>
    ///
    /// <returns> The factorial of num. </returns>
    static ulong IterativeFact(ulong num)
    {
        // It doesn't make sense to compute a negative factorial, so an error is
        // thrown in that case.
        if (num < 0)
        {
            throw new ArgumentOutOfRangeException(
                nameof(num), num, "Argument too small"
            );
        }
        
        ulong prod = 1;

        for (ulong n = 2; n <= num; n++)
        {
            prod *= n;
        }

        return prod;
    }

    /// <summary>
    ///     Computes a factorial using recursion.
    /// <br />
    /// <br />
    ///     Time complexity - O(N), where N is num.
    /// <br />
    ///     Space complexity - O(1).
    /// </summary>
    ///
    /// <param name="num"> The input number. </param>
    ///
    /// <returns> The factorial of num. </returns>
    static ulong RecursiveFact(ulong num)
    {
        // It doesn't make sense to compute a negative factorial, so an error is
        // thrown in that case.
        if (num < 0)
        {
            throw new ArgumentOutOfRangeException(
                nameof(num), num, "Argument too small"
            );
        }
        
        // The base case:
        if (num <= 1)
        {
            return 1;
        }
        else
        {
            return num * RecursiveFact(num - 1);
        }
    }
}