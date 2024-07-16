/**
 * A class that implements a queue data structure with an enqueue() and
 * dequeue() function. Internally, it uses an array to store all of the data.
 * 
 * @author Jared Austin Montgomery.
 */
class Queue {
    // Takes an array to use to store the queue items.
    constructor(arr) {
        this.arr = arr;
    }

    // Adds an item to the queue.
    enqueue(...items) {
        this.arr.push(...items);

        return this.arr.length;
    }

    // Removes an item to the queue.
    dequeue() {
        return this.arr.shift();
    }

    // Gives the number of items in the queue.
    length() {
        return this.arr.length;
    }
}