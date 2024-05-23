int main(void)
{
    ;
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