# Exercise:
# 12. Write a program that asks the user for a number and prints out the
# factorial of that number.

from utils import safe_input

def fact_iterative(x: int) -> int:
    """
    Summary:
        Calculates and returns the factorial of [x] using a for loop.

        Time complexity - O(N), where N is [x].
        Space complexity - O(1).
    
    Parameters:
        [x] - The number. Yep.
    """

    # Short for "product".
    prod: int = 1

    # Multiplies by every number between 2 and [x].
    for i in range(2, x + 1):
        prod *= i
    
    return prod

def fact_iterative_memo(x: int, results={}) -> int:
    """
    Summary:
        Calculates and returns the factorial of [x] using a for loop. Also, uses
        memoization.

        Time complexity - O(N), where N is [x].
        Space complexity - O(1).
    
    Parameters:
        [x] - The number. Yep.
    """

    if x in results:
        return results[x]

    # Short for "product".
    prod: int = 1

    # Multiplies by every number between 2 and [x].
    for i in range(2, x + 1):
        prod *= i
    
    results[x] = prod
    
    return results[x]

# Optional, just felt like making another approach.
def fact_recursive(x: int) -> int:
    """
    Summary:
        Calculates and returns the factorial of [x] using recursion.

        Time complexity - O(N), where N is [x].
        Space complexity - O(N).
    
    Parameters:
        [x] - The number. Yep.
    """

    if x < 2:
        return 1
    
    return x * fact_recursive(x - 1)

def fact_recursive_memo(x: int, results={}) -> int:
    """
    Summary:
        Calculates and returns the factorial of [x] using recursion. Also, uses
        memoization.

        Time complexity - O(N), where N is [x].
        Space complexity - O(N).
    
    Parameters:
        [x] - The number. Yep.
    """

    if x in results:
        return results[x]

    if x < 2:
        return 1
    
    results[x] = x * fact_recursive(x - 1)
    
    return results[x]

num: int = safe_input("Enter a number: ", int)

print(f"The factorial of {num} is {fact_iterative(num)}.")
