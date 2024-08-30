/**
 * This program simulates a number guessing game. At the start, the user is
 * asked to choose a lower and upper bound for the random number. After that,
 * they have to guess what it is with the game ending when they get it right.
 * 
 * Every time the user the user gets closer, it will say "Hotter.". Every time
 * the user gets further away, it will say "Colder.".
 */

#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(void)
{
    // Seeds the RNG.
    srand(time(NULL));

    int lower_bound, upper_bound;

    printf("Choose a lower bound between -32,767 and 32,767: ");
    scanf("%d", &lower_bound);

    printf("Choose a upper bound between -32,767 and 32,767: ");
    scanf("%d", &upper_bound);

    // Ensures that the upper bound is actually above the lower bound.
    while (upper_bound < lower_bound) {
        printf("Please choose a number bigger than %i for upper bound: ", lower_bound);
    }

    // Picks a random number between the lower and upper bound.
    int random_number = rand() % abs(upper_bound - lower_bound) + lower_bound;

    // The distance between the previous guess and the random number.
    int last_distance = -1;

    // Continues until the user gets it right.
    while (1) {
        int guess;

        printf("Make a guess between %i and %i: ", lower_bound, upper_bound);
        scanf("%d", &guess);

        if (guess == random_number) {
            printf("You won! %i is right.\n", guess);

            break;
        }

        int distance = abs(guess - random_number);

        if (distance < last_distance) {
            printf("Hotter.\n");
        } else if (distance > last_distance && last_distance != -1) {
            printf("Colder.\n");
        }

        last_distance = distance;
    }
}

/**
 * Algorithm:
 * 
 * - Have the user pick a lower and upper bound for the random number.
 * 
 * - Generate random number in that range.
 * 
 * - Make a loop that continues until the user guesses right.
 *
 *     - If the distance between this guess and the random number got smaller, then
 *     print "Hotter.".
 * 
 *     - If it got bigger, then print "Colder.".
 * 
 * - If the loop ends, then the user must've won.
 */