/*
 * The Collatz conjecture states that if you take a positive integer and repeat 2
 * operations on it (halving when even or multiplying by 3 and adding 1), then the
 * number should eventually reach 1. Is it true? Is it not? I don't know...
 * 
 * This program let you see the sequence of numbers you get when you repeatedly
 * apply the rules.
 */

#include <cstdio>

void print_collatz_seq(size_t num);

// If num is odd, then it is multiplied by this.
const int MULTIPLY_NUM = 3;
// If num is odd, then it is this is added to it.
const int ADD_NUM = 1;
// If num is even, then it is divided by this.
const int DIVIDE_NUM = 2;

// If 0, then the rules are normal. Otherwise, the rules are swapped.
const int SWAP_RULES = 0;

int main(void)
{
    // Prints the Collatz sequence for numbers from 0 to 20.
    for (size_t n = 0; n < 20; n++)
    {
        print_collatz_seq(n);
    }
}

/**
 * <pre>
 * Prints the Collatz sequence for a number. Each printed line will show a
 * number in the sequence and the number of steps it took to get there.
 * 
 * Time complexity - O(?). There's no telling how long it could take for a
 * randomly-given number.
 * Space complexity - O(1).
 * </pre>
 * 
 * @param num The starting number of the sequence. It's all down hill from here.
 */
void print_collatz_seq(size_t num)
{
    int step = 0;

    while (num != 1)
    {
        // Prints current number in sequence.
        std::printf("Step %i: %li \n", step, num);

        // Apply the rules.
        num = (num % 2 == SWAP_RULES) ? (num / DIVIDE_NUM) : (num * MULTIPLY_NUM + ADD_NUM);
        step++;
    }

    std::printf("Step %i: %li \n", step, num);
}
